#/bin/bash
#=====================================================
# MCMD bash script - Lesson 10: Calculation among rows with maccum 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=date,quantity,amount		i=${inPath}/dat.csv |
msortf f=date				|
msum k=date f=quantity:totalQuantity,amount:totalAmount		|
maccum f=totalQuantity:accumQuantity,totalAmount:accumAmount o=outdat/maccumout.csv

mcut f=CategoryCode2,CategoryCode4,quantity,amount      i=${inPath}/dat.csv |
msortf f=CategoryCode2,CategoryCode4%r          |
msum k=CategoryCode2,CategoryCode4 f=quantity,amount            |
maccum k=CategoryCode2 f=quantity:accumQuantity,amount:accumAmount o=outdat/maccumout0.csv

#=====================================================
