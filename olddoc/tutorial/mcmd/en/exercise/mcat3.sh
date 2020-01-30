#/bin/bash
#================================
# MCMD bash script - Lesson 13: Concatenate files 
#================================

# Variables
inPath="tutorial_en"

# Command 
mcat f=date,quantity,amount  			i=${inPath}/dat200104.csv,${inPath}/dat20011*.csv  | 
msortf f=date 					|
msum k=date f=quantity:totalQuantity,amount:totalAmount o=outdat/mcatout2.csv
#================================
