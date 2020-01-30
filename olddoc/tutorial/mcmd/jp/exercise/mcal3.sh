#!/bin/bash
#================================
# MCMD bash script - Lesson 11: Calculated fields 

# Variables
inPath="tutorial_jp"

# Command 

mcut f=日付 				i=${inPath}/dat.csv | 
msortf f=日付						|
muniq k=日付				| 
mcal c='$d{日付}+45'  a=45日後 		o=outdat/mcalout3.csv
#================================
