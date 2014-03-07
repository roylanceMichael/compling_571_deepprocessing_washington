####################
#
# Mike Roylance UW NetID roylance
# LING 571 Homework 6
#
####################
 
Universe   = vanilla
 
Executable  = hw6.sh
Arguments   = "ic-brown-resnik-add1.dat docs/wsd_contexts.txt docs/brown extraCredit-ic-brown.dat extraCreditResults results"
Log         = hw6.log
Output      = hw6.out
Error       = hw6.err
Notification= Error
getenv		= True
Queue