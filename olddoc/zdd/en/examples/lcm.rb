#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("tra.txt","w"){|fpw| fpw.write(
<<'EOF'
1 2 3 6
4 5 6
1 2 4 6
2 4 6
1 2 4 5
EOF
)}

File.open("order.txt","w"){|fpw| fpw.write(
<<'EOF'
1 2 3 4 5 6
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# Contents of tra.txt
# 1 2 3 6
# 4 5 6
# 1 2 4 6
# 2 4 6
# 1 2 4 5
# Contents of order.txt
# 1 2 3 4 5 6
p1=ZDD::lcm("FQ","tra.txt",3,"order.txt")
p1.show

# If order file is not specified, the resulting frequent itemset will be the same
# Note that the item number in the results is different from the item number
# in the transaction file.
p2=ZDD::lcm("FQ","tra.txt",3)
p2.show
EOF
run(scp,title,comment)

