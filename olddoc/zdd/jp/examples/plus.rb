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
c=ZDD::itemset("c")
x=3*a + 2*b
y=2*a + 2*b + 4*c
x.show
y.show
(x+y).show
EOF
run(scp,title,comment)

