#/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=CategoryCode2 			i=${inPath}/dat.csv |
msortf f=CategoryCode2                    	|
mcount k=CategoryCode2 a=numTransactions	o=outdat/mcountout4.csv
#=====================================================
