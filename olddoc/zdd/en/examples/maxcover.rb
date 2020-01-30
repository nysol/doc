#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# Set the cost of each item. 
ZDD::symbol("a",1.0)
ZDD::symbol("b",0.5)
ZDD::symbol("c",2.0)

a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")

f=a*b + b*c + c*a
f.show
# Cost of a b =1.0+0.5=1.5
# Cost of b c =0.5+2.0=2.5
# Cost of a c =1.0+2.0=3.0
puts f.maxcover
puts f.maxcost
puts f.mincover
puts f.mincost
EOF
run(scp,title,comment)

