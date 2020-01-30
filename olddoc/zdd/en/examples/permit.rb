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
y=a + b + d
z=a*c
x.show
y.show
z.show

# 4 itemsets a,bc,b,Φ (the term for empty itemset has a weight of 2) in x, 
# 3 itemsets a,b,d in y are included in itemset 
# a and b and Φ (empty itemset is also considered for inclusion as itemset).
# Therefore, select terms a,b,Φ from x. 
x.permit(y).show

# Among 4 itemsets a,bc,b,Φ contains in x, 
# itemset z contains ac, which includes itemset a and Φ. 
# Therefore, terms a and Φ are selected from x.
x.permit(z).show

# Among 4 itemsets a,bc,b,Φ contain in x, 
# itemset c includes itemset Φ. 
# Therefore, term Φ is selected from x.
x.permit(c).show
EOF
run(scp,title,comment)

