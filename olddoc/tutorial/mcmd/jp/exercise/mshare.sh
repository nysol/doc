#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 9: Calculation among rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=日付,数量,金額		i=${inPath}/dat.csv |
msortf f=日付				|
msum k=日付 f=数量,金額		|
mshare f=数量:数量シェア,金額:金額シェア o=outdat/mshareout.csv
#=====================================================
