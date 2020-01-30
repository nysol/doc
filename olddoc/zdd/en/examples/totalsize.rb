#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'

a=5*ZDD::itemset("a b c")-3*ZDD::itemset("a b")+2*ZDD::itemset("b c")+1*ZDD::itemset("c")
a.show
puts a.size
puts ZDD::totalsize

b=-3*ZDD::itemset("a c")
b.show
puts b.size
puts ZDD::totalsize
EOF
run(scp,title,comment)
