#/bin/bash
#=====================================================
# MCMD bash script - Lesson 8: Remove duplicate rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=date			i=${inPath}/dat.csv |
msortf f=date			|
muniq k=date    		o=outdat/muniqout.csv
#=====================================================
