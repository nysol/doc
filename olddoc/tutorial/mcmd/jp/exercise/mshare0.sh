#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 9: Calculation among rows 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=中分類,小分類,数量,金額			i=${inPath}/dat.csv |
msortf f=中分類,小分類				|
msum k=中分類,小分類 f=数量,金額		|
mshare k=中分類 f=数量:数量シェア,金額:金額シェア o=outdat/mshareout0.csv
#=====================================================
