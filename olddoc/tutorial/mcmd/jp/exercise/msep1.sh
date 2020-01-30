#/bin/bash
#================================
# MCMD bash script - Lesson 12: Separate files 
#================================
# Variables
inPath="tutorial_jp"

# Command 
msortf f=日付%n					i=${inPath}/dat.csv |
mcal c='cat("",n2s(year($d{日付})),n2s(month($d{日付})))' a="年月"     | 
msep d='tutorial_jp/dat${年月}.csv'    	
#================================
