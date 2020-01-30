#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
d=ZDD::itemset("d")
x=b*a*d + 5*b*c + 3*d + 4
x.show
x.csvout("output.csv")
# Contents of output.csv are as follows.
# Weight of 4 empty itemsets will be printed as nulll in the output.
# 1,a b d
# 5,b c
# 3,d
# 4,

# null ZDD object (empty itemsets with 0 weight) returns file with 0 byte.
y=ZDD::constant(0)
y.csvout("null.csv")
EOF
run(scp,title,comment)

