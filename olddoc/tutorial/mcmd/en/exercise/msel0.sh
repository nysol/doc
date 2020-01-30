#/bin/bash
#=====================================================
# MCMD bash script - Lesson 6: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
# Method 4
mcut f=date,quantity,amount 			i=${inPath}/dat.csv |
msel c='(${amount}/${quantity})<=100'		o=outdat/mselout0.csv

# Method 3 
mcut f=date,quantity,amount 			i=${inPath}/dat.csv |
msel c='${date}>20011015&&(${quantity}>5||${amount}>=1000)' o=outdat/mselout0.csv

mcut f=date,quantity,amount 			i=${inPath}/dat.csv |
msel c='${quantity}>5 && ${amount}>=1000'   	o=outdat/mselout0.csv
#=====================================================
