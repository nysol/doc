#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 10: Calculation among rows with maccum 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=中分類,メーカー,数量,金額		i=${inPath}/dat.csv |
msortf f=中分類,メーカー				|
msum k=中分類,メーカー f=数量,金額			|
maccum k=中分類 f=数量:数量累計,金額:金額累計 	o=outdat/maccumout2.csv

#=====================================================
