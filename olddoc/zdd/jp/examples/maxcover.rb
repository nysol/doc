#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# アイテムごとにコストを設定する。
ZDD::symbol("a",1.0)
ZDD::symbol("b",0.5)
ZDD::symbol("c",2.0)

a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")

f=a*b + b*c + c*a
f.show
# a b のコスト=1.0+0.5=1.5
# b c のコスト=0.5+2.0=2.5
# a c のコスト=1.0+2.0=3.0
puts f.maxcover
puts f.maxcost
puts f.mincover
puts f.mincost
EOF
run(scp,title,comment)

