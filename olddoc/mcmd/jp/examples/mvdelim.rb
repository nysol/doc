#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item1
b a c
c c
e a a
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
ベクトル型要素のデフォルトの区切り文字である半角スペースを\verb|_|(アンダーバー)に置換する。
EOF
scp=<<'EOF'
more dat1.csv
mvdelim vf=item1 v=_ i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例1
title="カンマ"
comment=<<'EOF'
CSVの区切り文字であるカンマに置換すると、CSVの区切り文字との区別を付けるために、
ベクトル全体がダブルクオーツで囲われる。
EOF
scp=<<'EOF'
mvdelim vf=item1 v=, i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

