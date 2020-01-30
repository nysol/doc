#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
k,n,p
0,2,0.5
1,2,0.5
2,2,0.5
4,10,0.2
40,100,0.2
3,2,0.2
1,2,1.2
EOF
)}

############## 例1 基本例
title="Example 1: Basic example"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='binomdist(${k},${n},${p})' a=prob i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

