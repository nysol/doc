#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,value
1,5
2,1
3,3
4,4
5,4
6,6
7,1
8,4
9,7
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
移動窓の合計を計算する。
最初の行は期数に満たないため出力されない。
EOF
scp=<<'EOF'
more dat1.csv
mmvstats s=id f=value t=2 c=sum i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
