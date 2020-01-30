#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# Define the value of symbol a, b, c as 1.0, 0.5, 1.8 accordingly.
ZDD::symbol("a",1.0)
ZDD::symbol("b",0.5)
ZDD::symbol("c",2.0)

a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")

# The expression creates a=1.0 for symbol a
puts a.cost

# a=1.0,b=0.5 is substituted into expression "a b" and becomes 1.0*0.5=0.5
f=a*b
f.show
puts f.cost

# a=1.0,b=0.5,c=2.0 is substituted into the expression "a b + 2 a + c + 3" and becomes
# 1.0*0.5+2*1.0+2.0+3=7.5
f=a*b + 2*a + c + 3
f.show
puts f.cost
EOF
run(scp,title,comment)

