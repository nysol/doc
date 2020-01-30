#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=大分類 			i=${inPath}/dat.csv |
msortf f=大分類                    	|
mcount k=大分類 a=行数           o=outdat/mcountout3.csv
#=====================================================
