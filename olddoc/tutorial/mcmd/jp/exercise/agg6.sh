#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 3: Aggregrate Functions 
# Exercise
#=====================================================
# Variables
inPath="tutorial_jp"

# Command 
mcut f=メーカー,中分類,数量,金額	i=${inPath}/dat.csv |
msortf f=メーカー,中分類                     |
msum k=メーカー,中分類 f=数量:数量合計,金額:金額合計  	o=outdat/aggout6.csv
#=====================================================
