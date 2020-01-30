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

# From all terms in the first argument of iif, select terms 2a, 3b which contains
# (a+b) with items a,b, and from all terms in the second argument of iif,
# select terms 8c, 9d which contains (a+b) with items a,b.
f=(a+b).iif(2*a+3*b+4*c+5*d,6*a+7*b+8*c+9*d)
f.show

# Used in conjunction with typical comparison operators as follows.
x=3*a+2*b+2*c
y=2*a+2*b+4*c
x.show
y.show

# Compare x and y, select term(s) where the weight of x is great than y, otherwise select y.
# If the result of x>y includes a, select 3a from the first argument x,
# Select the other itemsets 2b and 4c from the second argument y.
r1=(x>y).iif(x,y)
r1.show

# Compare x and y, select term(s) where the weight of x is greater than y.
# Similar to the above example, since the second term is 0,
# itemset other than a is not selected.
r2=(x>y).iif(x,0)
r2.show

# Compare x and y, select term(s) where the weight of x is the same weight as y.
r3=(x==y).iif(x,0)
r3.show
EOF
run(scp,title,comment)

