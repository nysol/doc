#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,quantity,price
A,0,1
B,1,0
C,2,200
D,3,0
E,0,298
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
item,price
fruit:apple,100
fruit:peach,250
fruit:grape,300
fruit:pineapple,450
fruit:orange,500
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
\verb|quantity|と\verb|price|項目が0をNULL値に置換する。
EOF
scp=<<'EOF'
more dat1.csv
mtonull f=quantity,price v=0 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="NULL値に置換する数字の指定"
comment=<<'EOF'
\verb|quantity|と\verb|price|項目が0もしくは1をNULL値に置換する。
EOF
scp=<<'EOF'
mtonull f=quantity,price v=0,1 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="部分文字列マッチでの置換"
comment=<<'EOF'
\verb|quantity|と\verb|price|項目が0を含めばNULL値に置換する。
EOF
scp=<<'EOF'
mtonull -sub f=quantity,price v=0 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="指定の文字列の置換"
comment=<<'EOF'
\verb|item|項目に\verb|apple、orange、pineapple|を含む値をNULL値に置換する。
EOF
scp=<<'EOF'
more dat2.csv
mtonull f=item v=apple,orange,pineapple -sub i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
