#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
items1,items2
b a c,10 2
c c,2 5 3
e a a,1
EOF
)}

############## Example 1
title="Sort multiple vectors"
comment=<<'EOF'
Sort \verb|item1| data series in ascending order and \verb|item2| in numerical ascending order.   
EOF
scp=<<'EOF'
more dat1.csv
mvsort vf=items1%r,items2%n i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
