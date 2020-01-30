#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
A,1
B,1
B,2
A,2
B,3
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|id|項目の値が連続しているときの累計を求める。\verb|-q|オプションを指定することで、
事前に\verb|k=|パラメータで指定した項目で並べ替える機能を無効化している。
EOF
scp=<<'EOF'
more dat1.csv
maccum -q k=id f=val:val_accum i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

