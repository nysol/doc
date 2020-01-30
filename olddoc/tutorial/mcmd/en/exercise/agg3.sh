#/bin/bash
#=====================================================
# MCMD bash script - Lesson 3: Aggregrate Functions 
# Exercise
#=====================================================
# Variables
inPath="tutorial_en"

# Command 
mcut f=date,quantity,amount 	i=${inPath}/dat.csv |
msortf f=date                    |
mstats k=date f=quantity:minQuantity,amount:minAmount c=min 	o=outdat/aggout3.csv
#=====================================================
