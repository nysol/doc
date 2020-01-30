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
数量と金額項目を切りだすが、出力データには項目名行は出力されない。
EOF
scp=<<'EOF'
more dat1.csv
mcut -nfno f=数量,金額 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

