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
Generate uniformly distributed random number from 0.0 to 1.0.
Since a random seed is specified, the random number sequence generated is always the same.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='rand(1)' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Random seed is not set"
comment=<<'EOF'
The random sequence will be different upon each run since random seed is not specified.
EOF
scp=<<'EOF'
mcal c='rand()' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

