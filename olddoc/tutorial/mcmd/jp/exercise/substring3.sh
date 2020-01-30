#/bin/bash
#=====================================================
# MCMD bash script - Lesson 5: Query by substring 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=時間,数量,金額 			i=${inPath}/dat.csv |
mcal c='hours($t{時間})' a=時 			| 
msortf f=時%n                       	 	| 
msum k=時 f="数量:数量合計,金額:金額合計" o=outdat/substringout3.csv
#=====================================================
