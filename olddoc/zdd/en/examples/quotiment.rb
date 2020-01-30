#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Division by constant"
comment=<<'EOF'
Division of valued sum of products x by constant c expressed in x/c,
where the weight (density) of each term in x is divided by c.

EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
x=13*a+3*b
x.show

# term a: quotient of 13/5 is 2 and thus becomes 2a. term b: quotient of 3/5 is 0 and
# thus not shown.
(x/5).show

# term a: remainder of 13/5 is 3 and thus becomes 3a. term b: remainder of 3/5 is 3 and
# thus becomes 3b.
(x%5).show

# restore the original value of x by multiplying the quotient with the divisor 5 and
# adding the reminder.
(5*(x/5)+(x%5)).show

EOF
run(scp,title,comment)

############## Example 2
title="Division by 1 itemset"
comment=<<'EOF'
 Division of valued sum of products x by itemset v expressed in x/v, where each term in x is divided by v.

Consider the operation is similar to a general polynomial.
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
x=7*a*b+5*b*c
y=7*a*b+5*b*c+2*c
x.show
y.show

# quotient of 7ab/b is 7a. quotient of 5bc/b is 5c.
(x/b).show

# remainder of 7ab/b is 0. remainder of 5bc/b is 0.
(x%b).show

# quotient of 7ab/3b is 2a. quotient of 5bc/3b is 1c. quotient of 2c/3b is 0 and thus not shown.
(y/(3*b)).show

# remainder of 7ab/3b is ab. remainder of 5bc/3b is 2bc. remainder of 2c/3b is 2c.
(y%(3*b)).show

# restore the original value of y by multiplying the quotient with the divisor 3b and
# adding the remainder.
(3*b*(y/(3*b))+(y%(3*b))).show
EOF
run(scp,title,comment)

############## Example 3
title="Division of 2 or more itemsets"
comment=<<'EOF'
Division of 2 valued sum of products x,y is computed as x/y.

Divisor y consists of multiple product terms $T_i$, find out $Q_i=x/T_i$ for all $i$.
$Q_i$ contains all common itemsets (terms),
where Q is defined as the absolute minimum value weight of the terms.


Note that this operation is different than general polynomial.
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
d=ZDD::itemset("d")

x=2*a*b+4*a*c+a*d-2*b*c+3*b*d
y=a+b
x.show
y.show

# x/y and x%y are computed as follows.
# Q1=(x/a)=2b +4c +d +0  +0  = 0  +2b +4c +d
# Q2=(x/b)=2a +0  +0 -2c +3d = 2a +0  -2c +3d
# Common itemsets for Q1 and Q2 are c and d, the absolute minimum value is -2c and d.
# The quotient is derived as follows.
(x/y).show
# compute x-(y*Q) to find out the remainder from the division of x%y.
(x%y).show

# Restore the original value of x by multiplying the quotient with the divisor y and
# adding the remainder.
(y*(x/y)+(x%y)).show
EOF
run(scp,title,comment)

