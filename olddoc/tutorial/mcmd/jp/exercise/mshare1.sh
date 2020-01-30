#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 9: Calculation among rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=メーカー,数量,金額		i=${inPath}/dat.csv |
msortf f=メーカー				|
msum k=メーカー f=数量,金額		|
mshare f=数量:数量シェア,金額:金額シェア  o=outdat/mshareout1.csv
#=====================================================
