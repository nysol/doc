#/bin/bash
#=====================================================
# MCMD bash script - Lesson 11: Create calculated fields 
# Exercise
#=====================================================

# Variables
inPath="tutorial_en"

# Command 
mcut f=customer,date		i=${inPath}/dat.csv |
msortf f=customer,date		|
mcal c='diffday(today(),$d{date})' a="dayDiff" o=outdat/mcaldayout.csv
#mcal c='diff(today(),$d{date},"day")' a="dayDiff" o=outdat/mcaldayout.csv

#mcal c='diff($d{date},0d20010102,"day")' a="dayDiff" o=outdat/mcaldayout.csv
#=====================================================
