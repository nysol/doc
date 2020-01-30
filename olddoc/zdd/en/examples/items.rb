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
f=((a*b*c)+(a*b)+(b*c))
f.show

# ZDD object f is made up of 3 items a, b, c. 
# The weight of each item is computed as follows. 
# The terms "a b c" and "2 a b" contains item a, the total weight is 3. 
# All terms contains item b, the total weight is 4.
# The terms "a b c" and "b c" contains item c, the total weight is 2. 
f.items.show
EOF
run(scp,title,comment)

