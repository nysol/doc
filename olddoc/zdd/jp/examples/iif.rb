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

# iifの第1引数の各項から、(a+b)に含まれるアイテムa,bの項2a,3bを選択し、
# iifの第2引数の各項から、(a+b)に含まれるアイテムa,bの項を除外した項8c,9dを選択する。
f=(a+b).iif(2*a+3*b+4*c+5*d,6*a+7*b+8*c+9*d)
f.show

# 典型的には比較演算子と組み合わせて以下のように利用する。
x=3*a+2*b+2*c
y=2*a+2*b+4*c
x.show
y.show

# xとyを比較し、yより大きい重みを持つ項をxから、それ以外をyから選ぶ。
# x>yの結果はaであり、第1引数xから3aが選択され、
# その他のアイテム集合は第2引数yから2b,4cが選ばれる。
r1=(x>y).iif(x,y)
r1.show

# xとyを比較し、yより大きい重みを持つ項をxから選ぶ。\\
# 上の例と同様であるが、第2引数が0なのでa以外のアイテム集合は何も選択されない。\\
r2=(x>y).iif(x,0)
r2.show

# xとyを比較し、yと同じ重みを持つ項をxから選ぶ。
r3=(x==y).iif(x,0)
r3.show
EOF
run(scp,title,comment)

