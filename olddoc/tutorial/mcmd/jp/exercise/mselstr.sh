#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 7: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=日付,数量,金額 			i=${inPath}/dat.csv |
mselstr f=日付 v=20010110,20010123,20010130   	o=outdat/mselstrout.csv
#=====================================================
