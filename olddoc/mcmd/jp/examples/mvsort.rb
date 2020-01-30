#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
items1,items2
b a c,10 2
c c,2 5 3
e a a,1
EOF
)}

############## 例1
title="複数項目を並べる例"
comment=<<'EOF'
\verb|item1|項目を文字列降順に並べ、\verb|item2|項目を数値昇順に並べる。
EOF
scp=<<'EOF'
more dat1.csv
mvsort vf=items1%r,items2%n i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
