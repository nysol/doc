#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=日付 				i=${inPath}/dat.csv |
msortf f=日付                    	|
mcount a=行数		o=outdat/mcountout.csv
#mcount k=日付 a=行数		o=outdat/mcountout.csv
#=====================================================
