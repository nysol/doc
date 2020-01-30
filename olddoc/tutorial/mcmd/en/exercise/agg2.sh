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
mstats k=date f=quantity:maxQuantity,amount:maxAmount c=max 	o=outdat/aggout2.csv
#=====================================================
