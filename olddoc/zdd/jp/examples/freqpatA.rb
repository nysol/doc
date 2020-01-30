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
t=a*b*c + a*b + a + b*c*d + a
t.show

# t=a*b*c + a*b + a + b*c*d + aにおいて、
# アイテム集合abは第1,2項の2回出現している。
# アイテム集合aは第1,2,3,5項の4回出現している。
t.freqpatA(2).show

# 極大アイテム集合(他のアイテム集合に包含されないアイテム集合)
# 上記頻出アイテム集合のうち、aはabに包含され、bとcはbcに包含され、
# 1は他の全てのアイテム集合に包含されていると考えるため、a,b,1は出力されない。
t.freqpatM(2).show

# 飽和アイテム集合(出現集合が同じアイテム集合族の中で極大のアイテム集合)
# 上記頻出アイテム集合のうち、bcとcのいずれも第1,4項に出現している。
# すなわち出現集合が同じアイテム集合族である。
# そしてそのなかで極大なbcのみが出力される。
# その他に列挙された飽和集合は全て異なる出現集合を持つ。
t.freqpatC(2).show

# 最小サポートを3にして実行する。
t.freqpatA(3).show
t.freqpatM(3).show
t.freqpatC(3).show
EOF
run(scp,title,comment)

