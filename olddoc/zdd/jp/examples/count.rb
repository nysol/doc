#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
f=a+b+a*b
f.show
puts f.count

g=a+b+a*b+1
g.show
puts g.count

c=ZDD::constant(0)
puts c.count

d=ZDD::constant(1)
puts d.count
EOF
run(scp,title,comment)

