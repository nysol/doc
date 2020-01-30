#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,10
B,1,15
A,2,20
B,3,10
B,1,20
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
「顧客」項目を単位に「数量」と「金額」項目の合計値を計算し、
「数量合計」と「金額合計」という項目名で出力する。
EOF
scp=<<'EOF'
more dat1.csv
msum k=顧客 f=数量:数量合計,金額:金額合計 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
