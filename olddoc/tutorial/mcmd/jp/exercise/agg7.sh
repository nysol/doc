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
mavg k=メーカー,中分類 f=数量:数量平均,金額:金額平均  	o=outdat/aggout7.csv
#=====================================================
