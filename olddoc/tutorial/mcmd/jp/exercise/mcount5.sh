#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=小分類			i=${inPath}/dat.csv |
msortf f=小分類                    	|
mcount k=小分類 a=行数	o=outdat/mcountout5.csv
#=====================================================
