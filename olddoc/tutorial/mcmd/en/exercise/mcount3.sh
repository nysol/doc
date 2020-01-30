#/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=CategoryCode1 			i=${inPath}/dat.csv |
msortf f=CategoryCode1                    	|
mcount k=CategoryCode1 a=numTransactions	o=outdat/mcountout3.csv
#=====================================================
