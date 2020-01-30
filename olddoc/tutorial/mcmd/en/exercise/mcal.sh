#/bin/bash
#================================
# MCMD bash script - Lesson 11: Create calculated fields 

# Variables
inPath="tutorial_en"

# Command 

mcut f=quantity,amount 		i=${inPath}/dat.csv | 
mcal c='${amount}/${quantity}' a=unitPrice 	|
mcut f=unitPrice				|
msortf f=unitPrice%n 				|
muniq k=unitPrice 		o=outdat/mcalout.csv
#================================
