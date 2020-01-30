#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")

# a,b,cの3アイテムを使った全組合せ数は8通り。
# 以下で、fにはそのすべての組合せが格納されているので濃度は1.0となる。
f=(a+1)*(b+1)*(c+1)
f.show
puts f.density

# 以下で、fには1通りの組合せ(a b)が格納されているので濃度は1/8=0.125となる。
f=a*b
f.show

puts f.density

# 以下で、fには3通りの組合せ(a b,a,b)が格納されているので濃度は3/8=0.375となる。
f+=a
f+=b
f.show
puts f.density
EOF
run(scp,title,comment)

