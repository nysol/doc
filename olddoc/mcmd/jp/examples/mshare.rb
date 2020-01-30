#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,10
A,2,20
B,1,15
B,3,10
B,1,20
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
「顧客」項目を単位に「数量」と「金額」項目のシェアを計算し、
「数量シェア」と「金額シェア」という項目名で出力する。
EOF
scp=<<'EOF'
more dat1.csv
mshare k=顧客 f=数量:数量シェア,金額:金額シェア i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
