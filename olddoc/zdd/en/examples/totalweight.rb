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
f=5*a + 3*b + c
f.show
puts f.totalweight

g=f - 10
g.show
puts g.totalweight
EOF
run(scp,title,comment)

