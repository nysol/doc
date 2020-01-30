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
title="Example 1: Basic example"
comment=<<'EOF'
Bernoulli random numbers are generated at probability $p = 0:2.$ Since a random number seed is specified, the same random number series will be generated no matter how many times the script is run.
EOF
scp=<<'EOF'
mnewnumber l=10 a=num |
mcal c='berrand(0.2,111)' a=rand o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="Example 2: 0,1 random integers"
comment=<<'EOF'
Generate two sets of random integers 0 and 1. The random sequence will be different upon each run since the random seed is not specified.
EOF
scp=<<'EOF'
mcal c='randi(0,1)' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
#run(scp,title,comment)

