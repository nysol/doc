#!/bin/bash
#=====================================================
# MCMD bash script - Lesson 11: Calculated fields 
# Exercise
#=====================================================

# Variables
inPath="tutorial_jp"

# Command 
mcut f=中分類,メーカー,数量,金額           	i=${inPath}/dat.csv |
msortf f=中分類,メーカー                         |
msum k=中分類,メーカー f=数量,金額  	         |
mshare k=中分類 f=数量:数量シェア,金額:金額シェア| 
mcal c='round(${数量シェア}*100,0.01)' a="数量シェアPCT" |
mcal c='round(${金額シェア}*100,0.01)' a="金額シェアPCT" o=outdat/mcal45out.csv
#=====================================================
