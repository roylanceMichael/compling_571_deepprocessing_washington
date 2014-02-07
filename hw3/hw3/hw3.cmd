Executable = run.sh
Arguments  = "/dropbox/13-14/571/hw3/data/parses.train /dropbox/13-14/571/hw3/data/sents.test"
universe   = vanilla
getenv     = true
error      = hw3.err
Log        = hw3.log
transfer_executable = false
request_memory = 2*1024
Queue
