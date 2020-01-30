#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id
1
2
3
4
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
0から始まる番号が出力される。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='line()' a=no i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="1から始める"
comment=<<'EOF'
1から始まる番号を出力する。
EOF
scp=<<'EOF'
mcal c='line()+1' a=no i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

