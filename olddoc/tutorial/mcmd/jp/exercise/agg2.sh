#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 3: Aggregrate Functions 
# Exercise
#=====================================================
# Variables
inPath="tutorial_jp"

# Command 
mcut f=日付,数量,金額 	i=${inPath}/dat.csv |
msortf f=日付                    |
mstats k=日付 f=数量:数量最大値,金額:金額最大値 c=max 	o=outdat/aggout2.csv
#=====================================================
