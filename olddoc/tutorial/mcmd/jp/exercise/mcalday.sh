#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 11: Create calculated fields 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=顧客,日付		i=${inPath}/dat.csv |
msortf f=顧客,日付		|
mcal c='diffday($d{日付},0d20010102)' a="日数" o=outdat/mcaldayout.csv

#mcal c='diffday(today(),$d{日付})' a="日数" o=outdat/mcaldayout.csv
#=====================================================
