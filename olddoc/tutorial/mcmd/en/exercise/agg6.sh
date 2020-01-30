#/bin/bash
#=====================================================
# MCMD bash script - Lesson 3: Aggregrate Functions 
# Exercise
#=====================================================
# Variables
inPath="tutorial_en"

# Command 
mcut f=manufacturer,CategoryCode4,quantity,amount 	i=${inPath}/dat.csv |
msortf f=manufacturer,CategoryCode4                      |
msum k=manufacturer,CategoryCode4 f=quantity:totalQuantity,amount:totalAmount  	o=outdat/aggout6.csv
#=====================================================
