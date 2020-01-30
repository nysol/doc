#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# a. Multiplication of constants.
# Weight is attached to sum of products term x by the expression x*c, the weight
# of each term in x is multiplied by c times.
# The computation is similar to general polynomial.
a=ZDD::itemset('a')
b=ZDD::itemset('b')
c=ZDD::itemset('c')
d=ZDD::itemset('d')
(a*3).show
(-2*a).show
((a+2*b+3*c)*4).show

# b. Multiplication by 1 itemset
# Weight is attached to sum of products term y by the expression x*y,
# y is added to the weight of each term in x.
# However, note that the multiplication beteween same items is expressed as a*a=a.
x=a+2*a*b+3*c
x.show
(x*c).show
(x*b).show
(4*x*a).show

# c. Multiplication of 2 or more itemsets
# Multiplication of the sum of products x,y which is attached with weight is computed
# by the expression x*y,
# The operation enumerates all possible combinations on the two product terms.
# Like terms such as a,b itemset are multiplied.
# The resulting expression includes addition and subtraction operations between
# enumerated item sets.
((a+b)*(c+d)).show
((a+b)*(b+c)).show
((a+b)*(a+b)).show
((a+b)*(a-b)).show
EOF
run(scp,title,comment)

