#!/bin/bash
#================================
# MCMD bash script - Lesson 13: Join 
#================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=小分類,数量,金額 		i=${inPath}/dat.csv | 
msortf f=小分類						|
msum k=小分類 f=数量,金額  	|
mjoin k=小分類 f=小分類名 m=${inPath}/jicfs4.csv		o=outdat/mjoinout.csv
#================================
