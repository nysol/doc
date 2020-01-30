#/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=date 				i=${inPath}/dat.csv |
msortf f=date                    	|
mcount k=date a=numTransactions		o=outdat/mcountout.csv
#mcount a=numTransactions		o=outdat/mcountout.csv
#=====================================================
