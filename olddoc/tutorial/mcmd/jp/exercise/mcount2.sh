#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=ブランド 				i=${inPath}/dat.csv |
msortf f=ブランド                    	|
mcount k=ブランド a=行数	o=outdat/mcountout2.csv
#=====================================================
