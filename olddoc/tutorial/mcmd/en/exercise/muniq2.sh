#/bin/bash
#=====================================================
# MCMD bash script - Lesson 8: Remove duplicate rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=manufacturer			i=${inPath}/dat.csv |
msortf f=manufacturer			|
muniq k=manufacturer    		o=outdat/muniqout2.csv
#=====================================================
