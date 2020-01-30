# bin/bash
#================================
# MCMD bash script - Lesson1: mcut
# Exercise - Extract manufacturer,brand and profit
#================================
# Variables
inPath="tutorial_en"

# Command 

mcut f=manufacturer,brand,profit i=${inPath}/dat.csv o=outdat/mcutout1.csv
#================================
