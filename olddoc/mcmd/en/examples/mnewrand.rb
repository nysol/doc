#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
Generate 10 rows of random integers. Use a fixed random seed so that it will always return the same sequence of random numbers.
EOF
scp=<<'EOF'
mnewrand a=rand S=1 o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Random Integers"
comment=<<'EOF'
Use random seed 1 to generate 5 rows of random integers with minimum value of 10 and maximum value of 100.
EOF
scp=<<'EOF'
mnewrand a=rand -int max=1000 min=0 l=5 S=1 o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Generate Output without Header"
comment=<<'EOF'
Specify \verb|-nfn| option to generate random number data without header.
EOF
scp=<<'EOF'
mnewrand -nfn l=5 S=1 o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
