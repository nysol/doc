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

############## Example 1
title="Basic Example"
comment=<<'EOF'
Create a set of random numbers with a standard deviation between 0 to 1  (standard normal distribution). Set the random seed as 10.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='nrand(0,1,10)' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

