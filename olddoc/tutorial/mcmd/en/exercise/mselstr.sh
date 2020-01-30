#/bin/bash
#=====================================================
# MCMD bash script - Lesson 7: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=date,quantity,amount 			i=${inPath}/dat.csv |
mselstr f=date v=20010110,20010123,20010130   	o=outdat/mselstrout.csv
#=====================================================
