#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,date,quantity,price
A,20081201,1,10
B,20081201,4,40
A,20081202,2,20
A,20081203,3,30
B,20081203,5,50
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|dat|という名前のディレクトリを作成し、
そのディレクトリに日付項目値\verb|date|ごとに異なるファイルに出力する。
EOF
scp=<<'EOF'
more dat1.csv
msep d='./dat/${date}.csv' -p i=dat1.csv
ls ./dat
more ./dat/20081201.csv
more ./dat/20081202.csv
more ./dat/20081203.csv
EOF
system("rm -rf dat")
run(scp,title,comment)

############## 例2
#title="並べ替わっていないとうまくいかない"
#comment=<<'EOF'
#\verb|item|項目をファイル名に指定すると、その項目で並べ替っていないのでうまくいかない。
#EOF
#scp=<<'EOF'
#msep d='./dat/${item}.csv' -p i=dat1.csv
#ls ./dat
#more ./dat/A.csv
#more ./dat/B.csv
#EOF
#system("rm -rf dat")
#run(scp,title,comment)
