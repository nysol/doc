#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
items1,items2
b a c,b
c c,
e a a,a a a
EOF
)}

############## 例1
title="複数項目に対して適用する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mvcount vf=items1:size1,items2:size2 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
