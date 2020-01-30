#!/bin/bash
#================================
# MCMD bash script - Lesson 12: Concatenate files 
#================================

# Variables
inPath="tutorial_jp"

# Command 
#mcat  				i=${inPath}/dat2001*.csv  o=outdat/mcatout.csv 

mcat f=日付,数量,金額  			i=${inPath}/dat2001*.csv | 
msortf f=日付%n 					|
msum k=日付 f=数量:数量合計,金額:金額合計 o=outdat/mcatout.csv
#================================
