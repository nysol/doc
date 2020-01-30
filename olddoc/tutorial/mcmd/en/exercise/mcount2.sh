#/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=brand 				i=${inPath}/dat.csv |
msortf f=brand                    	|
mcount k=brand a=numTransactions	o=outdat/mcountout2.csv
#=====================================================
