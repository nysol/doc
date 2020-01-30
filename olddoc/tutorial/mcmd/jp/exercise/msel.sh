#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 6: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=日付,数量,金額				i=${inPath}/dat.csv |
msel c='${日付}==20011020'		   	o=outdat/mselout.csv

# Command 
mcut f=日付,数量,金額				i=${inPath}/dat.csv |
mselstr f=日付 v=20011020		   	o=outdat/mselout.csv
#=====================================================
