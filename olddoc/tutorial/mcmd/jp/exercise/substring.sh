#/bin/bash
#=====================================================
# MCMD bash script - Lesson 5: Query by substring 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=日付,数量,金額 			i=${inPath}/dat.csv |
mcal c='cat("",n2s(year($d{日付})),n2s(month($d{日付})))' a="年月" | 
msortf f=年月%n                            |
msum k=年月 f=数量:数量合計,金額:金額合計      o=outdat/substringout.csv
#=====================================================
