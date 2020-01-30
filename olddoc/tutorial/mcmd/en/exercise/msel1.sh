#/bin/bash
#=====================================================
# MCMD bash script - Lesson 6: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=date,quantity,amount 			i=${inPath}/dat.csv |
msel c='${date}>20011020&&${amount}>1000' 	|
msortf f=date					|
msum k=date f=quantity:totalQuantity,amount:totalAmount o=outdat/mselout1.csv
#=====================================================
