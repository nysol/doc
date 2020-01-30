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
y=a + b + d
z=a*c
x.show
y.show
z.show

# xに含まれる4つのアイテム集合a,bc,b,Φ(重み2の項で空のアイテム集合)のうち、
# yの3つのアイテム集合a,b,dのいずれかに包含されるアイテム集合は
# aとbとΦ(空のアイテム集合はいずれのアイテム集合にも含まれると考える)。
# よって、xからa,b,Φの項が選択される。
x.permit(y).show

# xに含まれる4つのアイテム集合a,bc,b,Φのうち、zのアイテム集合acに含まれるアイテム集合はaとΦ。
# よって、xからaとΦの項が選択される。
x.permit(z).show

# xに含まれる4つのアイテム集合a,bc,b,Φのうち、アイテム集合cに含まれるアイテム集合はΦのみ。
# よって、xからΦの項が選択される。
x.permit(c).show
EOF
run(scp,title,comment)

