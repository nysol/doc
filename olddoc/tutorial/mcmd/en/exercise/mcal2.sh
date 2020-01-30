#/bin/bash
#================================
# MCMD bash script - Lesson 11: Calculated fields 

# Variables
inPath="tutorial_en"

# Command 

mcal c='round(${amount}*1.05,1)' a=taxAmount 	i=${inPath}/dat.csv | 
mcut f=date,taxAmount				| 
msortf f=date						|
msum k=date f=taxAmount:totalTaxAmount		o=outdat/mcalout2.csv
#================================
