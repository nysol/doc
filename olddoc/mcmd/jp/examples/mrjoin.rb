#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
price
8
15
35
50
90
200
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
range,category
10,low
35,middle
80,high
100,
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
item,price
A,10
A,20
B,10
B,20
EOF
)}

File.open("ref2.csv","w"){|fpw| fpw.write(
<<'EOF'
item,price,category
A,10,low
A,15,high
A,100,
B,10,low
B,35,high
B,100,
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|price|を範囲で
分類項目\verb|low、middle、high|を結合する。
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mrjoin r=price%n m=ref1.csv R=range f=category i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="基本例2"
comment=<<'EOF'
EOF
scp=<<'EOF'
mrjoin -lo r=price%n m=ref1.csv R=range f=category i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
############## 例3
title="基本例3"
comment=<<'EOF'
EOF
scp=<<'EOF'
mrjoin -n r=price%n m=ref1.csv R=range f=category i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
############## 例4
title="商品別に異なる範囲を設定して結合"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
more ref2.csv
mrjoin k=item r=price%n m=ref2.csv f=category i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)