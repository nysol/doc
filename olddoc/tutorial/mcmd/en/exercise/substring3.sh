#/bin/bash
#=====================================================
# MCMD bash script - Lesson 5: Query by substring 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=time,quantity,amount 			i=${inPath}/dat.csv |
mcal c='hours($t{time})' a="hour" 		| 
msortf f=hour%n                       	 	| 
msum k=hour f="quantity:totalQuantity,amount:totalAmount" |
mcut f=time -r 					o=outdat/substringout3.csv
#=====================================================
