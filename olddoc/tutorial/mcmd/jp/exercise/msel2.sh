#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 6: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=日付,時間,数量,金額 			i=${inPath}/dat.csv |
msel c='${日付}>170000&&(${金額}/${数量})<200' 	|
msortf f=日付                                    |
msum k=日付 f=数量:数量合計,金額:金額合計            |
mcut f=時間 -r 						o=outdat/mselout2.csv
#=====================================================
