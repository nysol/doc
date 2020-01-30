#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer
A
B
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
date
20090101
20090201
20090301
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
入力ファイルにある\verb|customer|項目に対して、
参照ファイルにある\verb|date|項目全行を結合する。
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mproduct f=date m=ref1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
