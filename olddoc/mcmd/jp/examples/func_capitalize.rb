#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,abc
2,aBd
3,
4,#abc
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
$str$項目の先頭文字を大文字に変換する。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='capitalize($s{str})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

