#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
store,val
A,2
B,
C,5
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
「数量」項目の値の数分、データを複写し複数行のデータを生成する。
対象項目がNULL値の場合は複写しない。
EOF
scp=<<'EOF'
more dat1.csv
mduprec f=val i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="複写行数の指定"
comment=<<'EOF'
データを2行づつ複写した(\verb|n=2|)データを生成する。
EOF
scp=<<'EOF'
mduprec n=2 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
