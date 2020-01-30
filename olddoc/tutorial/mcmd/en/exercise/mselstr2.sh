#/bin/bash
#=====================================================
# MCMD bash script - Lesson 7: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mselstr f=CategoryCode4 v=1101,1111,1115,1401,1403,1406 i=${inPath}/dat.csv |
mcut f=CategoryCode4,quantity,amount 		|
msortf f=CategoryCode4 				| 
msum k=CategoryCode4 f=quantity:totalQuantity,amount:totalAmount o=outdat/mselstrout2.csv
#=====================================================
