#/bin/bash
#=====================================================
# MCMD bash script - Lesson 6: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=date,time,quantity,amount 			i=${inPath}/dat.csv |
msel c='${time}>170000&&(${amount}/${quantity})<200' 	|
msortf f=date						|
msum k=date f=quantity:totalQuantity,amount:totalAmount |
mcut f=time -r 						o=outdat/mselout2.csv
#=====================================================
