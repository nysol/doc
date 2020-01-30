#!/bin/bash
#================================
# MCMD bash script - Lesson 11: Create calculated fields 

# Variables
inPath="tutorial_jp"

# Command 

mcut f=数量,金額 		i=${inPath}/dat.csv | 
mcal c='${金額}/${数量}' a=単価 	|
mcut f=単価				|
msortf f=単価%n 				|
muniq k=単価 		o=outdat/mcalout.csv
#================================
