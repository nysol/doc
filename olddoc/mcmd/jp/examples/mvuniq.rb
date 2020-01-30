#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
items1,items2
b a c,1 1
c c,2 2 3
e a a,3 1
EOF
)}

############## 例1
title="複数項目を単一化する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mvuniq vf=items1,items2 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
