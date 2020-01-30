#!/bin/bash
#================================
# MCMD bash script - Lesson 11: Calculated fields 

# Variables
inPath="tutorial_jp"

# Command 

mcut f=日付,数量,金額 			i=${inPath}/dat.csv | 
mavg k=日付 f=数量,金額			|
mcal c='round(${数量},1)' a=数量平均 	|
mcal c='round(${金額},1)' a=金額平均 	o=outdat/mcalout1.csv
#================================
