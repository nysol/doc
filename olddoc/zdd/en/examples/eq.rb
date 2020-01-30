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
x=3*a + 2*b + 2*c
y=2*a + 2*b + 4*c
x.show
y.show
# (x,y is defined above)

# Compare x and y, select itemsets with equal weight.
(x==y).show

# Compare x and y, select itemsets with weight that is greater than or equal to y.
(x>=y).show

# Compare x and y, select itemsets with unequal weights.
(x.ne?(y)).show

# For itemsets present in zdd1 but absent in zdd2 (or vice versa),
# the weight is considered as 0.
z=2*a + 2*b
z.show

# Since itemset c does not exists in z, the weight is considered as 0. 
(x>z).show
(x.ne?(z)).show
(x==z).show
EOF
run(scp,title,comment)

