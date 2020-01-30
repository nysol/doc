#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 7: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mselstr f=小分類 v=1101,1111,1115,1401,1403,1406 i=${inPath}/dat.csv |
mcut f=小分類,数量,金額  		|
msortf f=小分類 				| 
msum k=小分類 f=数量:数量合計,金額:金額合計 o=outdat/mselstrout2.csv
#=====================================================
