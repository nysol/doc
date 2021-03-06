#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# シンボルa, b, cに値1.0, 0.5, 1.8をそれぞれ与える。
ZDD::symbol("a",1.0)
ZDD::symbol("b",0.5)
ZDD::symbol("c",2.0)

a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")

# 式は1つのシンボルaから構成されa=1.0
puts a.cost

# 式"a b"にa=1.0,b=0.5を代入すると1.0*0.5=0.5
f=a*b
f.show
puts f.cost

# 式"a b + 2 a + c + 3"にa=1.0,b=0.5,c=2.0を代入すると 1.0*0.5+2*1.0+2.0+3=7.5
f=a*b + 2*a + c + 3
f.show
puts f.cost
EOF
run(scp,title,comment)

