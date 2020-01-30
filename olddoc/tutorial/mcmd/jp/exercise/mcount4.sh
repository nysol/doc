#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=中分類                      i=${inPath}/dat.csv |
msortf f=中分類                    	|
mcount k=中分類 a=行数               o=outdat/mcountout4.csv
#=====================================================
