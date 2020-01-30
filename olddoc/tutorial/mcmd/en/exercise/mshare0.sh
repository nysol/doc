#/bin/bash
#=====================================================
# MCMD bash script - Lesson 9: Calculation among rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=CategoryCode2,CategoryCode4,quantity,amount	i=${inPath}/dat.csv |
msortf f=CategoryCode2,CategoryCode4				|
msum k=CategoryCode2,CategoryCode4 f=quantity:totalQuantity,amount:totalAmount	|
mshare k=CategoryCode2 f=totalQuantity:quantityShare,totalAmount:amountShare o=outdat/mshareout0.csv
#=====================================================
