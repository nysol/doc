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

# Total number of combinations using 3 items a,b,c is eight.
# All combinations are stored in F in the expression below, with a density of 1.0.
f=(a+1)*(b+1)*(c+1)
f.show
puts f.density

# In the following, one set of combination (a b) is stored in F.
# The density becomes 1/8=0.125.f=a*b
f.show

puts f.density

# When three sets of combinations (a b,a,b) are stored in F, the density becomes 3/8=0.375.
f+=a
f+=b
f.show
puts f.density
EOF
run(scp,title,comment)

