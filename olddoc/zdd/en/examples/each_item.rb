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
f=2*a+2*b+4*a*c
f.each_item{|weight,item,top,bottom|
  puts weight
  item.show
  puts top
  puts bottom
  puts "----------"
}
EOF
system "echo #{scp} >xxscp" 
run(scp,title,comment)

