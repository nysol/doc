#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id
1
2
3
4
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
100から999(3桁整数900種類)の整数乱数を生成する。
乱数の種を指定しているので、何度実行しても同じ乱数系列が生成される。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='randi(100,999,1)' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="0,1の整数乱数"
comment=<<'EOF'
0と1の2種類の整数乱数を生成する。
乱数の種を指定していないので、実行の度に異なる乱数系列が生成される。
EOF
scp=<<'EOF'
mcal c='randi(0,1)' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

