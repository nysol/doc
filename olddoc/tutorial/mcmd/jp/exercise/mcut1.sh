#!/bin/bash
#================================
# MCMD bash script - Lesson1: mcut
# Exercise - Extract manufacturer,brand and profit
# Variables
inPath="tutorial_jp"

# Command 

mcut f=メーカー,ブランド,粗利金額 i=${inPath}/dat.csv o=outdat/mcutout1.csv
#================================
