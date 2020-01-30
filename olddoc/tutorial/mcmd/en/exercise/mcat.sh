#/bin/bash
#================================
# MCMD bash script - Lesson 13: Concatenate files 
#================================

# Variables
inPath="tutorial_en"

# Command 
mcat f=date,quantity,amount 		i=${inPath}/dat2001*.csv |tee x| 
msortf f=date%n 					|
msum k=date f=quantity:totalQuantity,amount:totalAmount o=outdat/mcatout.csv
#================================
