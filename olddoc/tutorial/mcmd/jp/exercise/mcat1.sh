#!/bin/bash
#================================
# MCMD bash script - Lesson 13: Concatenate files 
#================================

# Variables
inPath="tutorial_jp"

# Command 
mcat f=日付,数量,金額 	i=${inPath}/dat20014.csv,${inPath}/dat20015.csv,${inPath}/dat20017.csv  | 
msortf f=日付 					|
msum k=日付 f=数量:数量合計,金額:金額合計 o=outdat/mcatout1.csv
#================================
