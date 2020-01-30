#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 3: Aggregrate Functions 

# Variables
inPath="tutorial_jp"

# Command 
mcut f=日付,数量,金額 	 	i=${inPath}/dat.csv |
msortf f=日付                    |
msum k=日付 f=数量:数量合計,金額:金額合計 	o=outdat/msumout.csv

#=====================================================
