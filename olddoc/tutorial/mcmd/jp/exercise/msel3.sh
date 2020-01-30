#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 6: Select records 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
msel c='${メーカー}==0300'      			i=${inPath}/dat.csv | 
mcut f=日付,数量,金額                     |	
msortf f=日付                             |
msum k=日付 f=数量:数量合計,金額:金額合計     o=outdat/mselout3.csv
#=====================================================
