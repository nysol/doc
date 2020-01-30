#!/bin/bash
#================================
# MCMD bash script - Lesson 11: Calculated fields 

# Variables
inPath="tutorial_jp"

# Command 

mcal c='round(${金額}*1.05,1)' a=税込金額 	i=${inPath}/dat.csv | 
mcut f=日付,税込金額				| 
msortf f=日付						|
msum k=日付 f=税込金額			o=outdat/mcalout2.csv
#================================
