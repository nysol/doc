#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'

f=5*ZDD::itemset("a b c")-3*ZDD::itemset("a b")+2*ZDD::itemset("b c")+1*ZDD::itemset("c")
f.show
puts f.size
EOF
run(scp,title,comment)

