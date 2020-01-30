#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,date,quantity,price
B,20081201,4,40
A,20081201,10,200
A,20081201,10,100
B,20081203,5,50
B,20081201,2,500
A,20081201,3,300
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|item、date|順に並べ替える。
EOF
scp=<<'EOF'
more dat1.csv
msortf f=item,date i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="数量(quantity)降順，金額(price)昇順に並べ替える例"
comment=<<'EOF'
EOF
scp=<<'EOF'
msortf f=quantity%nr,price%n i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
