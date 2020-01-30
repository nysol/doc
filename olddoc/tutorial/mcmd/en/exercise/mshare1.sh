#/bin/bash
#=====================================================
# MCMD bash script - Lesson 9: Calculation among rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=manufacturer,quantity,amount		i=${inPath}/dat.csv |
msortf f=manufacturer				|
msum k=manufacturer f=quantity,amount		|
mshare f=quantity:quantityShare,amount:amountShare o=outdat/mshareout1.csv
#=====================================================
