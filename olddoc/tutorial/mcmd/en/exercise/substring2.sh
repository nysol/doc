#/bin/bash
#=====================================================
# MCMD bash script - Lesson 5: Query by substring 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=date,quantity,amount 			i=${inPath}/dat.csv |
mcal c='day($d{date})' a="day" 			| 
msortf f=day%n                       	 	| 
msum k=day f="quantity:totalQuantity,amount:totalAmount" |
mcut f=date -r 					o=outdat/substringout2.csv
#=====================================================
