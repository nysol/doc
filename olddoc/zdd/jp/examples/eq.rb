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
x=3*a + 2*b + 2*c
y=2*a + 2*b + 4*c
x.show
y.show
# (x,yが上記の通り定義されていたとする)

# xとyを比較し、同じ重みを持つアイテム集合を選択する。
(x==y).show

# xとyを比較し、y以上の重みを持つアイテム集合を選択する。
(x>=y).show

# xとyを比較し、異なる重みを持つアイテム集合を選択する。
(x.ne?(y)).show

# zdd1にあってzdd2にない(もしくはその逆)アイテム集合の重みは0と考えればよい。
z=2*a + 2*b
z.show

# アイテム集合cはzにないので項0cを考えればよい。
(x>z).show
(x.ne?(z)).show
(x==z).show
EOF
run(scp,title,comment)

