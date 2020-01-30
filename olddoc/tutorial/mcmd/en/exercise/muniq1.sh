#/bin/bash
#=====================================================
# MCMD bash script - Lesson 8: Remove duplicate rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=brand			i=${inPath}/dat.csv |
msortf f=brand			|
muniq k=brand    		o=outdat/muniqout1.csv
#=====================================================
