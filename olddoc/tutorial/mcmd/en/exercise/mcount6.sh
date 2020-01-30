#/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=manufacturer,CategoryCode2 			i=${inPath}/dat.csv |
msortf f=manufacturer,CategoryCode2                    	|
mcount k=manufacturer,CategoryCode2 a=numTransactions	o=outdat/mcountout6.csv
#=====================================================
