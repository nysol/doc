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
x=5*a + 3*b + b*c + 2
x.show

# アイテムが1つ以下のアイテム集合を選択
x.permitsym(1).show

# アイテムが2つ以下のアイテム集合を選択
x.permitsym(2).show

# アイテムのないアイテム集合(すなわち空アイテム集合)を選択
x.permitsym(0).show
EOF
run(scp,title,comment)

