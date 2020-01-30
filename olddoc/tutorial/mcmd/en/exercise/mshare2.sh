#/bin/bash
#=====================================================
# MCMD bash script - Lesson 9: Calculation among rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=CategoryCode2,manufacturer,quantity,amount		i=${inPath}/dat.csv |
msortf f=CategoryCode2,manufacturer				|
msum k=CategoryCode2,manufacturer f=quantity,amount		|
mshare k=CategoryCode2 f=quantity:quantityShare,amount:amountShare o=outdat/mshareout2.csv
#=====================================================
