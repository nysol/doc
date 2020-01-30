#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
t,x,y
1,14,0.17
2,11,0.2
3,32,0.15
4,13,0.33
5,8,0.1
6,19,0.56
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|x、y|項目についてのピアソンの積率相関係数を3期を窓として計算する。
EOF
scp=<<'EOF'
more dat1.csv
mmvsim s=t t=3 c=pearson f=x,y a=sim i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)