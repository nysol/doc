#/bin/bash
#================================
# MCMD bash script - Lesson 14: Join 
#================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=CategoryCode2,quantity,amount		i=${inPath}/dat.csv | 
msortf f=CategoryCode2						|
msum k=CategoryCode2 f=quantity:totalQuantity,amount:totalAmount 	|
mjoin k=CategoryCode2 f=Category2 m=${inPath}/jicfs2.csv		o=outdat/mjoinout1.csv
#================================
