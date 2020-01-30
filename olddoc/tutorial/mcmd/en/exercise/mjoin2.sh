#/bin/bash
#================================
# MCMD bash script - Lesson 14: Join 
#================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=CategoryCode6,quantity,amount		i=${inPath}/dat.csv | 
msortf f=CategoryCode6						|
msum k=CategoryCode6 f=quantity:totalQuantity,amount:totalAmount 	|
mjoin k=CategoryCode6 f=Category6 m=${inPath}/jicfs6.csv		o=outdat/mjoinout2.csv
#================================
