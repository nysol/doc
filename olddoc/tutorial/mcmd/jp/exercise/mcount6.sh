#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 4: Aggregrate Functions II 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=メーカー,中分類 				i=${inPath}/dat.csv |
msortf f=メーカー,中分類                    	|
mcount k=メーカー,中分類 a=行数      o=outdat/mcountout6.csv
#=====================================================
