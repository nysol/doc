#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 8: Remove duplicate rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=ブランド			i=${inPath}/dat.csv |
msortf f=ブランド			|
muniq k=ブランド    		o=outdat/muniqout1.csv
#=====================================================
