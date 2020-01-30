#/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=CategoryCode4 			i=${inPath}/dat.csv |
msortf f=CategoryCode4                    	|
mcount k=CategoryCode4 a=numTransactions	o=outdat/mcountout5.csv
#=====================================================
