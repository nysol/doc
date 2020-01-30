#!/bin/bash
#================================
# MCMD bash script - Lesson 13: Join 
#================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=中分類,数量,金額		i=${inPath}/dat.csv | 
msortf f=中分類						|
msum k=中分類 f=数量,金額 	|
mjoin k=中分類 f=中分類名 m=${inPath}/jicfs2.csv		o=outdat/mjoinout1.csv
#================================
