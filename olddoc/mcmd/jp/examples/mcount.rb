#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
date
20090109
20090109
20090110
20090109
20090110
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|date|項目を単位に行数をカウントし、\verb|count|という項目名で出力する。
EOF
scp=<<'EOF'
more dat1.csv
mcount k=date a=count i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="集計キーなし"
comment=<<'EOF'
集計キーを指定しなければ全体の行数をカウントする。
EOF
scp=<<'EOF'
mcount a=count i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

