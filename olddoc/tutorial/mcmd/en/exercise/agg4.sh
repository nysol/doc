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
msum k=CategoryCode2 f=quantity:totalQuantity,amount:totalAmount  	o=outdat/aggout4.csv
#=====================================================
