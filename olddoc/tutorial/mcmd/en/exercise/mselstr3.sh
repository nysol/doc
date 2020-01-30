#/bin/bash
#=====================================================
# MCMD bash script - Lesson 7: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=amount:amount_key,quantity,amount 		 i=${inPath}/dat.csv |
mselstr f=amount v=199,299,399 				| 
msortf f=amount_key 					| 
msum k=amount_key f=quantity:totalQuantity,amount:totalAmount o=outdat/mselstrout3.csv
#=====================================================
