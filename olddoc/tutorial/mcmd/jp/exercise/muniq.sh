#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 8: Remove duplicate rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=日付			i=${inPath}/dat.csv |
msortf f=日付			|
muniq k=日付    		o=outdat/muniqout.csv
#=====================================================
