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
f=((a*b*c)+(a*b)+(b*c))
f.show

# ZDDオブジェクトfは3つのアイテムa,b,cから構成されており、
# それぞれのアイテムの重みを以下の通り計算する。
# アイテムaを含む項は"a b c"と"2 a b"で、その重み合計は3となる。
# アイテムbは全ての項に含まれ、その重み合計は4となる。
# アイテムcを含む項は"a b c"と"b c"で、その重み合計は2となる。
f.items.show
EOF
run(scp,title,comment)

