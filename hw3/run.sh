#! /bin/bash

(python2.7 ./source_Olga/source/main.py $1 $2;

/dropbox/13-14/571/hw3/tools/evalb -p /dropbox/13-14/571/hw3/tools/COLLINS.prm /dropbox/13-14/571/hw3/data/parses.test parses.hyp > parses.hyp.eval)
