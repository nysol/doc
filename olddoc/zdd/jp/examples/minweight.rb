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
x=5*a-3*b+c
x.show
x.minweight.show

# 最大値は定数項も含めて求められる。
x=5*a-3*b+c-10
x.show
x.minweight.show

# 最大の重みを持つ項を選択する。
x=5*a-3*b+5*c-3
x.show
x.termsEQ(x.minweight).show
EOF
run(scp,title,comment)

