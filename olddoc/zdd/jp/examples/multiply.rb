#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# a. 定数乗算
# 重み付き積和集合xに定数cを掛けるx*cでは、xの各項の重みをc倍する。
# 通常の多項式と同様に考えれば良い。
a=ZDD::itemset('a')
b=ZDD::itemset('b')
c=ZDD::itemset('c')
d=ZDD::itemset('d')
(a*3).show
(-2*a).show
((a+2*b+3*c)*4).show

# b. 1つのアイテム集合の乗算
# 重み付き積和集合xに1つのアイテム集合yを掛けるx*yでは、xの各項目にアイテム集合yを加える。
# ただし、同じアイテム同士の掛け算 a*a=a となることに注意する。
x=a+2*a*b+3*c
x.show
(x*c).show
(x*b).show
(4*x*a).show

# c. 2つ以上のアイテム集合の乗算
# 2つの重み付き積和集合x,yの乗算x*yでは、xとyそれぞれの各項から一つずつ選ぶ組み合わせ全てについて
# 上記a,bの乗算を付す。
# 乗算の結果同じアイテム集合の項は加減算される。
((a+b)*(c+d)).show
((a+b)*(b+c)).show
((a+b)*(a+b)).show
((a+b)*(a-b)).show
EOF
run(scp,title,comment)

