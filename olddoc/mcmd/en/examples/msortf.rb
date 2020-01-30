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

############## Example 1
title="Basic example"
comment=<<'EOF'
Sort by \verb|item| and \verb|date|.
EOF
scp=<<'EOF'
more dat1.csv
msortf f=item,date i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Sort by quantity in descending order and price in ascending order."
comment=<<'EOF'
EOF
scp=<<'EOF'
msortf f=quantity%nr,price%n i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
