# bin/bash
#============================================================
# MCMD bash script - Lesson 1: mcut command
# Exercise - Extract customer ID and reciept number 

# Variables
inPath="tutorial_en"

# Command 

mcut f=customer,receipt i=${inPath}/dat.csv o=outdat/mcutout2.csv
#============================================================
