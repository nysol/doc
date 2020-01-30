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
x=5*a + b*c + 3*b + 2
x.show

# xに含まれる4つのアイテム集合a,bc,b,Φ(重み2の項で空のアイテム集合)のうち、
# yの2つのアイテム集合a,bのいずれかを包含するアイテム集合は、a,bcである。
# よってxからa,bcの項が選択される。
x.restrict(a+c).show

# xに含まれる4つのアイテム集合a,bc,b,Φのうち、
# zのアイテム集合bcを包含するアイテム集合は、bcのみ。
# よってxからbcの項が選択される。
x.restrict(b*c).show

# xに含まれる4つのアイテム集合a,bc,b,Φのうち、
# アイテム集合Φ(重み1の空アイテム集合)を含むアイテム集合は全てのアイテム集合。
x.restrict(1).show

# xに含まれる4つのアイテム集合a,bc,b,Φのうち、アイテム集合abcを含むアイテム集合はない。
x.restrict(a*b*c).show
EOF
run(scp,title,comment)

