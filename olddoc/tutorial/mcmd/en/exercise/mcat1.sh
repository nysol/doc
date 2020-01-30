#/bin/bash
#================================
# MCMD bash script - Lesson 13: Concatenate files 
#================================

# Variables
inPath="tutorial_en"

# Command 
mcat f=date,quantity,amount 			i=${inPath}/dat20014.csv,${inPath}/dat20015.csv,${inPath}/dat20017.csv  | 
msortf f=date 					|
msum k=date f=quantity:totalQuantity,amount:totalAmount o=outdat/mcatout1.csv
#================================
