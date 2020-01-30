#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 8: Remove duplicate rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=メーカー			i=${inPath}/dat.csv |
msortf f=メーカー			|
muniq k=メーカー    		o=outdat/muniqout2.csv
#=====================================================
