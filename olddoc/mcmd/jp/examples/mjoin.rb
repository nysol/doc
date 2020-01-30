#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,date,price
A,20081201,100
A,20081213,98
B,20081002,400
B,20081209,450
C,20081201,100
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,cost
A,50
B,300
E,200
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
入力ファイルにある\verb|item|項目と、
参照ファイルにある\verb|item|項目を比較し同じ値の場合、\verb|cost|項目を結合する。
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mjoin k=item f=cost m=ref1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="未結合データ出力"
comment=<<'EOF'
入力ファイルにある\verb|item|項目と、
参照ファイルにある\verb|item|項目を比較し同じ値の場合、\verb|cost|項目を結合する。
その際、参照データにない入力データと参照データにない範囲データをNULL値として出力する。
EOF
scp=<<'EOF'
mjoin k=item f=cost m=ref1.csv -n -N i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
