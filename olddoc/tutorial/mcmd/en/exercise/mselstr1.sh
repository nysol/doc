#/bin/bash
#=====================================================
# MCMD bash script - Lesson 7: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mselstr f=manufacturer v=0054,0085,1110    	i=${inPath}/dat.csv |
mcut f=manufacturer,quantity,amount 		|
msortf f=manufacturer 				| 
msum k=manufacturer f=quantity:totalQuantity,amount:totalAmount o=outdat/mselstrout1.csv
#=====================================================
