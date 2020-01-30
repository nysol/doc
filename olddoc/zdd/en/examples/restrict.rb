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
x=5*a + b*c + 3*b + 2
x.show

# Among 4 itemsets a,bc,b,Φ (empty itemset has a weight of 2) in x,  
# 2 itemsets a,b in y included in any of the itemset are a,bc. 
# Therefore terms a,bc are selected from x.
x.restrict(a+c).show

# Among 4 itemsets a,bc,b,Φ in x, 
# itemset z only includes itemset bc.
# Therefore term bc is selected from x.
x.restrict(b*c).show

# Among 4 itemsets a,bc,b,Φ in x,  
# all itemsets containing itemset Φ (empty itemsets with weight of 1) is in a set of items.
x.restrict(1).show

# Among 4 itemsets a,bc,b,Φ in x, there is no itemset contained in itemset abc.
x.restrict(a*b*c).show
EOF
run(scp,title,comment)

