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
puts a.diff?(b)
puts a.diff?(a)
puts (a+b).diff?(a+c)
puts (a+b).diff?(a+b)
EOF
run(scp,title,comment)

