#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=メーカー 				i=${inPath}/dat.csv |
msortf f=メーカー                    	|
mcount k=メーカー a=行数		o=outdat/mcountout1.csv
#=====================================================
