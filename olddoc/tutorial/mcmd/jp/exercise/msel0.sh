#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 6: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command
# Method 4 
mcut f=日付,数量,金額 				i=${inPath}/dat.csv |
msel c='(${金額}/${数量})<=100'		o=outdat/mselout0.csv

# Method 3 
mcut f=日付,数量,金額 				i=${inPath}/dat.csv |
msel c='${日付}>20011015&&(${数量}>5||${金額}>=1000)' o=outdat/mselout0.csv

mcut f=日付,数量,金額                     i=${inPath}/dat.csv |
msel c='${数量}>5 && ${金額}>=1000'       o=outdat/mselout0.csv


#=====================================================
