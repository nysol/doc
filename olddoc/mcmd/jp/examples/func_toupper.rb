#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,abc
2,Ab$12!cD
3,
4,Cba
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
$str$項目のアルファベット小文字を全て大文字に変換する。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='toupper($s{str})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

