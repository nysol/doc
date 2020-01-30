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
f=5*a + 3*b + c
f.show

# 3の重みを持つ項を選択する。
f.termsEQ(3).show

# 3以上の重みを持つ項を選択する。
f.termsGE(3).show

# 3でない重みを持つ項を選択する。
f.termsNE(3).show

# 条件に合う項がなければ0
f.termsGT(10).show
EOF
run(scp,title,comment)

