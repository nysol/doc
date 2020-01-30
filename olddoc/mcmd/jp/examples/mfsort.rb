#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,v1,v2,v3
1,b,a,c
2,a,b,a
3,b,,e
EOF
)}

############## Example 1
title="例1: 基本例"
comment=<<'EOF'
各行において \verb|v1,v2,v3| の値を昇順にならべ、その順番で \verb|v1,v2,v3| 項目として出力する。
EOF
scp=<<'EOF'
more dat1.csv
mfsort f=v* i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="例2: 降順"
comment=<<'EOF'
降順にしたければ\verb|-r|を付ける。
EOF
scp=<<'EOF'
mfsort f=v* -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

