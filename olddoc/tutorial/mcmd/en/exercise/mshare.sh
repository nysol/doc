#/bin/bash
#=====================================================
# MCMD bash script - Lesson 9: Calculation among rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=date,quantity,amount		i=${inPath}/dat.csv |
msortf f=date				|
msum k=date f=quantity,amount		|
mshare f=quantity:quantityShare,amount:amountShare o=outdat/mshareout.csv
#=====================================================
