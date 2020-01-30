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
c.show
# The operation between ZDD weight object and Ruby character string,
# where Ruby character string is read as an itemset and automatically cast as ZDD object.
(c*"a").show

# The operation between ZDD weight object and Ruby integer, where Ruby integer is
# treated as ZDD weight object.
(0*c).show

# ZDD weight object is converted to Ruby integer, and the operation is carried out
# in Ruby integer.
puts c.to_i*10

# In the following example, the weight is defined as 0. This object is automatically cast
# to RubyString for computation.
a=ZDD::constant(0)
a+="x"
a+="x z"
a+="z"
a.show
EOF
run(scp,title,comment)

