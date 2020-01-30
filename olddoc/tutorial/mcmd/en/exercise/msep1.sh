#/bin/bash
#================================
# MCMD bash script - Lesson 12: Separate files 
#================================
# Variables
inPath="tutorial_en"

# Command 
msortf f=date%n					i=${inPath}/dat.csv |
mcal c='cat("",n2s(year($d{date})),n2s(month($d{date})))' a="YearMonth"     | 
msep d='tutorial_en/dat${YearMonth}.csv'    	
#================================
