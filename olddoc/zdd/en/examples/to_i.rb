#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
c=ZDD::constant(10)
c.show           # ZDD constant object
puts c.to_i      # ruby integer

# Return nil if not ZDD constant object. 
a=ZDD::itemset("a")
p a.to_i
EOF
run(scp,title,comment)

