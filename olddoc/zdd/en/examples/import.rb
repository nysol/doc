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
f=5*a*b*c+3*a*b+2*b*c+c
f.show
f.export("dat.zdd")
# Contents in the export file dat.zdd are as follows. 
# _i 3
# _o 3
# _n 7
# 4 1 F T
# 248 2 F 5
# 276 3 4 248
# 232 2 F 4
# 2 2 F T
# 272 3 232 2
# 268 3 232 248
# 276
# 272
# 268
EOF
run(scp,title,comment)

title="Example of correctly restored file"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# After sybmol is declared in order, import correctly restores the file. 
ZDD::symbol("a")
ZDD::symbol("b")
ZDD::symbol("c")
g1=ZDD::import("dat.zdd")
g1.show
EOF
run(scp,title,comment)

title="Example of incorrectly restored file"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# If item b,c are not declared in order, b and c will be represented incorrectly
# in the results.
ZDD::symbol("a")
ZDD::symbol("c")
ZDD::symbol("b")
g2=ZDD::import("dat.zdd")
g2.show
EOF
run(scp,title,comment)

title="Restore file without symbol declaration"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# Item names such as x1,x2,x3 will be used if the symbols are not declared before import. 
# In this case, the sequence number followed after x will be in reverse order
# corresponding to the declaration order of the item.
# In the following example, x1=c, x2=b, x3=c.
g3=ZDD::import("dat.zdd")
g3.show
EOF
run(scp,title,comment)

