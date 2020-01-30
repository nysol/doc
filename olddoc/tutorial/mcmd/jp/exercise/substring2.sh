#/bin/bash
#=====================================================
# MCMD bash script - Lesson 5: Query by substring 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=日付,数量,金額 	 			i=${inPath}/dat.csv |
mcal c='day($d{日付})' a="日" 			| 
msortf f=日%n                       	 	| 
msum k=日 f="数量:数量合計,金額:金額合計" o=outdat/substringout2.csv
#=====================================================