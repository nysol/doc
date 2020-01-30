#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 10: Calculation among rows with maccum 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=日付,数量,金額		i=${inPath}/dat.csv |
msortf f=日付				|
msum k=日付 f=数量:数量合計,金額:金額合計		|
maccum f=数量合計:数量累計,金額合計:金額累計 o=outdat/maccumout.csv

mcut f=中分類,小分類,数量,金額 	i=${inPath}/dat.csv |
msortf f=中分類,小分類%r		| 
msum k=中分類,小分類 f=数量,金額	| 
maccum k=中分類 f=数量:数量累計,金額:金額累計 o=outdat/maccumout0.csv
#=====================================================
