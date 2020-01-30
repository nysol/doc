#!/bin/bash
#================================
# MCMD bash script - Lesson 13: Join 
#================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=細分類,数量,金額		i=${inPath}/dat.csv | 
msortf f=細分類						|
msum k=細分類 f=数量,金額 	|
mjoin k=細分類 f=細分類名 m=${inPath}/jicfs6.csv		o=outdat/mjoinout2.csv
#================================
