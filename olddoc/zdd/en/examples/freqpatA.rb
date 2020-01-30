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
t=a*b*c + a*b + a + b*c*d + a
t.show

# At the expression t=a*b*c + a*b + a + b*c*d + a,
# Itemset ab appeared twice in first and second term.
# Itemset a appeared four times in first, second, third, and fifth term.
t.freqpatA(2).show

# Maximal itemset (itemsets that are not included in other itemsets)
# Among the frequent itemsets above, a is included in ab, b and c is include in bc,
# Considering 1 will be included in other itemsets, a,b,1 will not be returned as output.
t.freqpatM(2).show

# Closed itemsets (emerged itemsets are in the same itemset group as in maximal itemset)
# Among the above frequent itemsets, bc and c appeared as 1st and 4th term.
# The emerged itemsets belong to the same itemset group.
# Within this group, only bc is the maximum.
# Other emumerated closed itemsets emeraged as a different group.
t.freqpatC(2).show

# Run the three functions with a minimum support of 3.
t.freqpatA(3).show
t.freqpatM(3).show
t.freqpatC(3).show
EOF
run(scp,title,comment)

