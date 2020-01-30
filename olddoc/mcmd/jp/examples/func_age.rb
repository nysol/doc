#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,dob
1,19641010
2,20000101
3,
4,19770812
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
2013年9月1日における年令を求める。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='age($d{dob},0d20130901)' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

