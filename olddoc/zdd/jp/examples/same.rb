#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
puts a.same?(b)
puts a.same?(a)
puts (a+b).same?(a+c)
puts (a+b).same?(a+b)
puts (a-a).same?(0)
puts (2*a/a)===2
EOF
run(scp,title,comment)

