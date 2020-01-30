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
mavg k=date f=quantity:avgQuantity,amount:avgAmount 	o=outdat/aggout1.csv
#=====================================================
