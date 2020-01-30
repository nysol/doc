#/bin/bash
#=====================================================
# MCMD bash script - Lesson 3: Aggregrate Functions 
# Exercise
#=====================================================
# Variables
inPath="tutorial_en"

# Command 
mcut f=CategoryCode2,quantity,amount 	i=${inPath}/dat.csv |
msortf f=CategoryCode2                      |
mavg k=CategoryCode2 f=quantity:avgQuantity,amount:avgAmount  	o=outdat/aggout5.csv
#=====================================================
