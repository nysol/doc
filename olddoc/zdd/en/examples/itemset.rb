#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a b")
a.show
b=ZDD::itemset("b")
b.show
c=ZDD::itemset("")
c.show

# Numbers can be used as name of item
x0=ZDD::itemset("2")
x0.show

# However, bear in mind that it  may be difficult to distinguish between weight and
# numerical item name.
(2*x0).show

# Symbols can be used as name of item 
x1=ZDD::itemset("!#%&'()=~|@[;:]")
x1.show

# However, special symbols in Ruby must be escaped with a backward slash (\).
# In the following example, the 3 characters \,$," are escaped. 
x2=ZDD::itemset("\\\$\"")
x2.show

# Japanese characters can be used to name an item as well. 
x3=ZDD::itemset("りんご ばなな")
x3.show
EOF
run(scp,title,comment)

