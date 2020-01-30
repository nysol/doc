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
f=5*a*b*c - 3*a*b + 2*b*c + c
f.show
ZDD::constant(0).show
EOF
run(scp,title,comment)

############## Example 2
title="bit"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
f=5*a*b*c - 3*a*b + 2*b*c + c
f.show

f.bit

# "a b c" has weight of -5, expressed in (-2) base is 101. 
# 1*(-2)^2+0*(-2)^1+1*(-2)^0 = 5
# Therefore 0 digit and 2nd digit of itemset "a b c" is display. 
# "a b" has weight of -3 expressed in (-2) base is 1101. 
# 1*(-2)^3+1*(-2)^2+0*(-2)^1+1*(-2)^0 = -3
# Therefore 0,2nd,3rd digit of itemset "a b" is displayed. 
EOF
run(scp,title,comment)

############## Example 3
title="hex"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
d=ZDD::itemset("d")

f=a*b+11*b*c+30*d+4
f.show
f.hex
EOF
run(scp,title,comment)

############## Example 4
title="map"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
d=ZDD::itemset("d")
f=2*a*b+3*b+4
f.show
f.map
# Itemset is displayed with item a as the first sequence in the bit string,
# and item b corresponds to the first row of the bit string.
# Weight is displayed as the cell value. Upper left cell contains 0 in a, and 0 in b,
# and constant term 4 is shown.

# The 4 items are as follows. 
g=a*b + 2*b*c + 3*d + 4
g.show
g.map
EOF
run(scp,title,comment)

############## Example 5
title="rmap"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# Declare 4 items a,b,c,d
ZDD::symbol("a")
ZDD::symbol("b")
ZDD::symbol("c")
ZDD::symbol("d")

f=ZDD::itemset("a b") + 2*ZDD::itemset("b c") + 4
f.show

# The following displays as map.
f.map

# d is omitted when displayed as rmap. 
f.rmap
EOF
run(scp,title,comment)

############## Example 6
title="case"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
f=5*a*b*c - 3*a*b + 2*b*c + 5*c
f.show

f.case
EOF
run(scp,title,comment)

############## Example 7
title="decomp"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")

f1=(a*b*c)
f1.show
f1.decomp
# AND of a,b,c is expressed as a*b*c=a b c

f2=((a*b*c)+(a*b))
f2.show
f2.decomp
# OR of c,1 is expressed as (c+1), in addition, AND of a b is expressed as (a b),
# the complete expression becomes (a b)*(c+1)=a b c + a b

f3=((a*b*c)+(a*b)+(b*c))
f3.show
f3.decomp
# [ a c ] enumerates all combinations from a and c as (a c + a + c).
# AND of b and the above expression becomes b*(a c + a + c) = a b c + a b + b c

f4=((a*b*c)+(a*b)+(b*c)+(c*a))
f4.show
f4.decomp
# [ a b c ] enumerates all combinations from a,b,c as (a b c + a b + b c + c a)
EOF
run(scp,title,comment)
