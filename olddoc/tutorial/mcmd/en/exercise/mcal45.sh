#/bin/bash
#=====================================================
# MCMD bash script - Lesson 11: Calculated fields 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command
mcut f=CategoryCode2,manufacturer,quantity,amount           i=${inPath}/dat.csv |
msortf f=CategoryCode2,manufacturer                         |
msum k=CategoryCode2,manufacturer f=quantity,amount         |
mshare k=CategoryCode2 f=quantity:quantityShare,amount:amountShare | 
mcal c='round(${quantityShare}*100,0.01)' a="qtySharePct" |
mcal c='round(${amountShare}*100,0.01)' a="amtSharePct" o=outdat/mcal45out.csv
 
#=====================================================
