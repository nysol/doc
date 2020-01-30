#/bin/bash
#================================
# MCMD bash script - Lesson 11: Calculated fields 

# Variables
inPath="tutorial_en"

# Command 

mcut f=date 				i=${inPath}/dat.csv | 
msortf f=date						|
muniq k=date				| 
mcal c='$d{date}+45'  a=newDate		o=outdat/mcalout3.csv
#================================
