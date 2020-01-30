#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id
1
2
3
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,a
2,
3,b
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
rslという項目の全行にNULL値を出力する。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='nulls()' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="if文の中での利用"
comment=<<'EOF'
if文の第二パラメータで数値を指定しているので、それに合わせてnulln()関数を用いる。
EOF
scp=<<'EOF'
mcal c='if(${id}==1,1,nulln())' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="isnullと同等の指定"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='if(${val}==nulln(),"null","notNull")' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

