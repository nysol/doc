#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
c=ZDD::constant(10)
c.show           # ZDD定数オブジェクト
puts c.to_i      # ruby整数

# ZDD定数オブジェクトでなければnilとなる。
a=ZDD::itemset("a")
p a.to_i
EOF
run(scp,title,comment)

