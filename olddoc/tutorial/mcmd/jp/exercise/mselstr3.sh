#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 7: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=金額:金額キー,数量,金額  		 i=${inPath}/dat.csv |
mselstr f=金額 v=199,299,399 				| 
msortf f=金額キー                             | 
msum k=金額キー f=数量:数量合計,金額:金額合計 o=outdat/mselstrout3.csv
#=====================================================
