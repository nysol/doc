#/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=manufacturer 				i=${inPath}/dat.csv |
msortf f=manufacturer                    	|
mcount k=manufacturer a=numTransactions		o=outdat/mcountout1.csv
#=====================================================
