#/bin/bash
#=====================================================
# MCMD bash script - Lesson 10: Calculation among rows with maccum 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=manufacturer,quantity,amount		i=${inPath}/dat.csv |
msortf f=manufacturer				|
msum k=manufacturer f=quantity,amount		|
maccum f=quantity:accumQuantity,amount:accumAmount o=outdat/maccumout1.csv

#=====================================================
