#/bin/bash
#=====================================================
# MCMD bash script - Lesson 2: Sort 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=date,quantity,amount 		i=${inPath}/dat.csv |
msortf f=date%r                       	|	
msum k=date f=quantity:totalQuantity,amount:totalAmount	o=outdat/msortfout.csv
#=====================================================
