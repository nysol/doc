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
Generate random integers from 100 to 999 (3 digit integers 900 types). Since a random seed is specified, the random number sequence generated is always the same.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='randi(100,999,1)' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="0,1 random integers"
comment=<<'EOF'
Generate two sets of random integers 0 and 1. The random sequence will be different upon each run since the random seed is not specified.
EOF
scp=<<'EOF'
mcal c='randi(0,1)' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

