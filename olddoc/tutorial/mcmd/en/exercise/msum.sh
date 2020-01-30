#/bin/bash
#=====================================================
# MCMD bash script - Lesson 3: Aggregrate Functions 

# Variables
inPath="tutorial_en"

# Command 
mcut f=date,quantity,amount 	i=${inPath}/dat.csv |
msortf f=date                    |
msum k=date f=quantity:totalQuantity,amount:totalAmount 	o=outdat/msumout.csv
#=====================================================
