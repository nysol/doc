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
f=a+2*a*b+3*b

# Find out the intersection of itemset a with each term in the expression a + 2ab + 3b, 
# the result becomes a + 2a + 3 = 3 a + 3.
f.meet(a).show

# The intersection with itemset b becomes 1 + 2b + 3b = 5b + 1.
f.meet(b).show

# The intersection with itemset ab becomes a + 2ab + 3b.
f.meet(a*b).show

# Empty itemset is represented by constant number 1, thus the intersection with 1
# with all coefficients becomes 1 + 2 + 3 = 6.
f.meet(1).show

# Find out the interaction of each itemset in abc + 2ab + bc + 1 with each itemset 
# in the specified argument 2ab + a as follows (remove space between items) 
# abc ∩ 2ab = 2ab
# 2ab ∩ 2ab = 4ab
# bc  ∩ 2ab = 2b
# 1   ∩ 2ab = 2
# abc ∩ a   = a
# 2ab ∩ a   = 2a
# bc  ∩ a   = 1
# 1   ∩ a   = 1
# The result is summarized as 6ab + 3a + 2b + 4.
#
f=((a*b*c)+2*(a*b)+(b*c)+1)
g=2*a*b + a
f.show
g.show
f.meet(g).show
EOF
run(scp,title,comment)

