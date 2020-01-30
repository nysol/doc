#/bin/bash
#=====================================================
# MCMD bash script - Lesson 6: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
msel c='${manufacturer}==0300||${manufacturer}==0320'  	i=${inPath}/dat.csv |
mcut f=date,quantity,amount 				|	
msortf f=date						|
msum k=date f=quantity:totalQuantity,amount:totalAmount o=outdat/mselout4.csv
#=====================================================
