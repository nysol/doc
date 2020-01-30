#/bin/bash
#=====================================================
# MCMD bash script - Lesson 6: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
# Method 1
mcut f=date,quantity,amount 			i=${inPath}/dat.csv |
msel c='${date}==20011020'		   	o=outdat/mselout.csv


# Method 1
mcut f=date,quantity,amount 			i=${inPath}/dat.csv |
mselstr f=date v=20011020		   	o=outdat/mselout.csv
#=====================================================
