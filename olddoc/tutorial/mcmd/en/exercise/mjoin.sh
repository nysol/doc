#/bin/bash
#================================
# MCMD bash script - Lesson 14: Join 
#================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=CategoryCode4,quantity,amount		i=${inPath}/dat.csv | 
msortf f=CategoryCode4							|
msum k=CategoryCode4 f=quantity:totalQuantity,amount:totalAmount 	|
mjoin k=CategoryCode4 f=Code4Details m=${inPath}/jicfs4.csv		o=outdat/mjoinout.csv
#================================
