#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
items1,items2,items3,items4
b a c,b,x,y
c c,,x,y
e a a,a a a,x,y
EOF
)}

############## 例1
title="ワイルドカードを利用した例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mvcat vf=items* a=items i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
