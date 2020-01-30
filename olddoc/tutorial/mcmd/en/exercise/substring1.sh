#/bin/bash
#=====================================================
# MCMD bash script - Lesson 5: Query by substring 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=date,quantity,amount 			i=${inPath}/dat.csv |
mcal c='month($d{date})' a="month" 		| 
msortf f=month%n                       	 	| 
msum k=month f="quantity:totalQuantity,amount:totalAmount" |
mcut f=date -r 					o=outdat/substringout1.csv
#=====================================================
