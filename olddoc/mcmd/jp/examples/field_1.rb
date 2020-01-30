#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
ブランド,数量10,数量11,数量12
A,10,15,9
B,20,16,8
C,30,17,7
D,40,18,6
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
A,10,15,9
B,20,16,8
C,30,17,7
D,40,18,6
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
項目名による指定と項目番号による指定。
EOF
scp=<<'EOF'
more dat1.csv
mcut f=ブランド,数量11 i=dat1.csv o=rsl1.csv
more rsl1.csv
mcut f=0,2 -x i=dat1.csv o=rsl2.csv
more rsl2.csv
more dat2.csv
mcut f=0,2 -nfn i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

