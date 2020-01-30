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
x=5*a + 3*b + b*c + 2
x.show

# Select itemsets with less than or equal to 1 item 
x.permitsym(1).show

# Select itemsets with less than or equal to 2 items
x.permitsym(2).show

# Select itemsets without any item (that is empty itemsets) 
x.permitsym(0).show
EOF
run(scp,title,comment)

