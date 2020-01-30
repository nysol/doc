#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 2: Sort 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=日付,小分類,数量,金額             i=${inPath}/dat.csv |
msortf f=日付%r,小分類%n                 		|
msum k=日付,小分類 f=数量:数量合計,金額:金額合計	|
msortf f=日付%r,数量合計%nr 			o=outdat/msortfout4.csv
#=====================================================
