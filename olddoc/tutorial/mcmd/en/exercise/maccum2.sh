#/bin/bash
#=====================================================
# MCMD bash script - Lesson 10: Calculation among rows with maccum 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=CategoryCode2,manufacturer,quantity,amount	i=${inPath}/dat.csv |
msortf f=CategoryCode2,manufacturer				|
msum k=CategoryCode2,manufacturer f=quantity,amount		|
maccum k=CategoryCode2 f=quantity:accumQuantity,amount:accumAmount o=outdat/maccumout2.csv

#=====================================================
