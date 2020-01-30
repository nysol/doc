#!/bin/bash
#============================================================
# MCMD bash script - Lesson 1: mcut command
# Exercise - Extract customer ID and reciept number 

# Variables
inPath="tutorial_jp"

# Command 

mcut f=顧客,レシート  i=${inPath}/dat.csv o=outdat/mcutout2.csv
#============================================================
