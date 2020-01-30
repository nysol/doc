#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 10: Calculation among rows with maccum 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=メーカー,数量,金額		i=${inPath}/dat.csv |
msortf f=メーカー				|
msum k=メーカー f=数量,金額			|
maccum f=数量:数量累計,金額:金額累計 	o=outdat/maccumout1.csv

#=====================================================
