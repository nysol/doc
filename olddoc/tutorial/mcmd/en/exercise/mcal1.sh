#/bin/bash
#================================
# MCMD bash script - Lesson 11: Calculated fields 

# Variables
inPath="tutorial_en"

# Command 

mcut f=date,quantity,amount 		i=${inPath}/dat.csv | 
mavg k=date f=quantity,amount			|
mcal c='round(${quantity},1)' a=avgQuantity 	|
mcal c='round(${amount},1)' a=avgAmount 	o=outdat/mcalout1.csv
#================================
