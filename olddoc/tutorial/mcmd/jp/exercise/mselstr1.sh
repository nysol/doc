#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 7: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mselstr f=メーカー  v=0054,0085,1110    	i=${inPath}/dat.csv |
mcut f=メーカー,数量,金額                |
msortf f=メーカー                       |
msum k=メーカー f=数量:数量合計,金額:金額合計 o=outdat/mselstrout1.csv
#=====================================================
