#/bin/bash
#=====================================================
# MCMD bash script - Lesson 2: Sort 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=date,CategoryCode4,quantity,amount 		i=${inPath}/dat.csv |
msortf f=date%r,CategoryCode4%n                 		|	
msum k=date,CategoryCode4 f=quantity:totalQuantity,amount:totalAmount	|
msortf f=date%r,totalQuantity%nr 			o=outdat/msortfout4.csv
#=====================================================
