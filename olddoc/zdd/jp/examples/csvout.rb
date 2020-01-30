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
d=ZDD::itemset("d")
x=b*a*d + 5*b*c + 3*d + 4
x.show
x.csvout("output.csv")
# output.csvの内容は以下の通り。
# 重み4の空のアイテム集合はnullが出力される。
# 1,a b d
# 5,b c
# 3,d
# 4,

# nullのZDDオブジェクト(重み0の空のアイテム集合)は0バイトファイルとなる。
y=ZDD::constant(0)
y.csvout("null.csv")
EOF
run(scp,title,comment)

