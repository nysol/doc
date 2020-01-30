#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="定数除算"
comment=<<'EOF'
重み付き積和集合xの定数cによる除算x/cは、
xの各項(アイテム集合)の重み(頻度)をcで整数除算した商を重みに持つアイテム集合が計算される。
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
x=13*a+3*b
x.show

# aの項:13/5の商は2であるから2a。bの項:3/5の商は0であるから0bとなり表示されない。
(x/5).show

# aの項:13/5の余りは3であるから3a。bの項:3/5の余りは3であるから3bとなる。
(x%5).show

# 除数の5に商を掛けて余りを足せば元の値xに戻る。
(5*(x/5)+(x%5)).show

EOF
run(scp,title,comment)

############## 例2
title="1つのアイテム集合による除算"
comment=<<'EOF'
重み付き積和集合xのアイテム集合vによる除算x/vは、xの各項をvで除する演算である。
通常の多項式と同様に考えれば良い。
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
x=7*a*b+5*b*c
y=7*a*b+5*b*c+2*c
x.show
y.show

# 7ab/bの商は7a。5bc/bの商は5c。
(x/b).show

# 7ab/bの余りは0。5bc/bの余り0。
(x%b).show

# 7ab/3bの商は2a。5bc/3bの商は1c。2c/3bの商は0となり表示されない。
(y/(3*b)).show

# 7ab/3bの余りはab。5bc/3bの余りは2bc。2c/3bの余りは2c。
(y%(3*b)).show

# 除数の3bに商を掛けて余りを足せば元の値yに戻る。
(3*b*(y/(3*b))+(y%(3*b))).show
EOF
run(scp,title,comment)

############## 例3
title="2つ以上のアイテム集合による除算"
comment=<<'EOF'
2つの重み付き積和集合x,yの除算x/yは次のように計算される。
除数yの各項を$T_i$としたとき$Q_i=x/T_i$を全ての$i$について求める。
得られた$Q_i$全てに共通して含まれるアイテム集合(項)について、
重みの絶対値が最小の項を商Qと定義する。
通常の多項式とは異なることに注意する。
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
d=ZDD::itemset("d")

x=2*a*b+4*a*c+a*d-2*b*c+3*b*d
y=a+b
x.show
y.show

# x/yおよびx%yは以下のように計算される。
# Q1=(x/a)=2b +4c +d +0  +0  = 0  +2b +4c +d
# Q2=(x/b)=2a +0  +0 -2c +3d = 2a +0  -2c +3d
# Q1,Q2で共通のアイテム集合はcとdであり、それぞれで絶対値が最小の項は-2cとdである。
# よって求める商は以下の通りとなる。
(x/y).show
# x%yについてはx-(y*Q)を計算すればよい。
(x%y).show

# 除数yに商を掛けて余りを足せば元の値xに戻る。
(y*(x/y)+(x%y)).show
EOF
run(scp,title,comment)

