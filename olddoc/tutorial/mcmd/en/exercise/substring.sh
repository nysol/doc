#/bin/bash
#=====================================================
# MCMD bash script - Lesson 5: Query by substring 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=date,quantity,amount 			i=${inPath}/dat.csv |
mcal c='cat("",n2s(year($d{date})),n2s(month($d{date})))' a="YearMonth" | 
msortf f=YearMonth%n                       	| 
msum k=YearMonth f=quantity:totalQuantity,amount:totalAmount   |
mcut f=date -r 					o=outdat/substringout.csv
#=====================================================
