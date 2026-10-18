args <- commandArgs(TRUE)
flavor <- if(length(args)>=3) args[[3]] else 'patched'
.libPaths(c(file.path(args[[4]],flavor),.libPaths()))
library(datapond)
cat('R',R.version.string,'duckdb',as.character(packageVersion('duckdb')),'datapond',as.character(packageVersion('datapond')),'\n')
cfg <- list(memory_limit='128MiB',threads='1',max_temp_directory_size='0B',autoinstall_known_extensions='false')
options(datapond.registry_url=args[[1]],datapond.cache_dir=args[[2]],datapond.duckdb_config=cfg)
driver <- duckdb::duckdb(config=cfg)
probe <- DBI::dbConnect(driver)
stopifnot(isTRUE(DBI::dbGetQuery(probe,"SELECT installed FROM duckdb_extensions() WHERE extension_name='httpfs'")$installed[[1]]))
DBI::dbDisconnect(probe,shutdown=TRUE)
if(flavor=='cran') {
  originalDuckdb <- duckdb::duckdb
  testthat::local_mocked_bindings(duckdb=function(...) originalDuckdb(...,config=cfg),.package='duckdb')
  cat('CRAN driver constructor bounded by test harness; datapond functions unchanged.\n')
}
# dp_connect calls INSTALL; replace only that instruction in this process with
# LOAD of the preinstalled extension. No software download/install is allowed.
originalExecute <- DBI::dbExecute
testthat::local_mocked_bindings(dbExecute=function(conn,statement,...) {
  if(grepl('INSTALL httpfs',statement,fixed=TRUE)) statement <- gsub('INSTALL httpfs','LOAD httpfs',statement,fixed=TRUE)
  originalExecute(conn,statement,...)
},.package='DBI')
con <- dp_connect('fars',quiet=TRUE)
tryCatch({
 stopifnot(DBI::dbGetQuery(con,'SELECT count(*) AS n FROM accident')$n[[1]]==36297)
 stopifnot(nrow(dp_describe(con))==4,nrow(dp_describe(con,table='accident'))==80)
 stopifnot(DBI::dbGetQuery(con,'SELECT count(*) AS n FROM _columns')$n[[1]]==413)
 x <- DBI::dbGetQuery(con,'SELECT count(*) AS crashes,sum(fatals) AS fatalities,sum(vehicle_records) AS vehicles,sum(person_records) AS people FROM crashes')
 stopifnot(x$crashes[[1]]==36297,x$fatalities[[1]]==39254,x$vehicles[[1]]==56011,x$people[[1]]==88326)
 print(x)
 missing <- DBI::dbGetQuery(con,'SELECT age,age_years,alc_res,measured_bac_g_dl FROM people WHERE age=999 AND alc_res=999 LIMIT 1')
 stopifnot(nrow(missing)==1,is.na(missing$age_years[[1]]),is.na(missing$measured_bac_g_dl[[1]]))
 print(dplyr::collect(utils::head(dplyr::tbl(con,'crashes'),3)))
 cat('R localhost HTTP consumer PASS\n')
},finally=dp_disconnect(con))
