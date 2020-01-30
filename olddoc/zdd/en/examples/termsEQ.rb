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

# Select terms with weight of 3. 
f.termsEQ(3).show

# Select terms with weight greater than or equal to 3.
f.termsGE(3).show

# Select terms with weight not equal to 3.
f.termsNE(3).show

# Return 0 if none of the terms herein matches the condition. 
f.termsGT(10).show
EOF
run(scp,title,comment)

