#/bin/bash
#=====================================================
# MCMD bash script - Lesson 3: Aggregrate Functions 

# Variables
inPath="tutorial_en"

# Command 
mcut f=date,quantity,amount 	i=${inPath}/dat.csv |
msortf f=date                    |
#mstats k=date f=quantity:totalQuantity,amount:totalAmount c=sum         o=outdat/mstatsout.csv
mstats k=date f=quantity:sdQuantity,amount:sdAmount c=sd         o=outdat/mstatsout.csv
#=====================================================
