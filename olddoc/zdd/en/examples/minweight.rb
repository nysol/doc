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
x=5*a-3*b+c
x.show
x.minweight.show

# The maximum constant term is returned. 
x=5*a-3*b+c-10
x.show
x.minweight.show

# Select the term with the maximum weight.
x=5*a-3*b+5*c-3
x.show
x.termsEQ(x.minweight).show
EOF
run(scp,title,comment)

