#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
c=ZDD::constant(10)
c.show
# ZDD重みオブジェクトとruby文字列との演算では、
# ruby文字列はアイテム集合と見なされ自動でZDDオブジェクトにキャストされる。
(c*"a").show

# ZDD重みオブジェクトとruby整数との演算では、ruby整数はZDD重みオブジェクトと見なされる。
(0*c).show

# ZDD重みオブジェクトをruby整数に変換し、ruby整数として演算する。
puts c.to_i*10

# 以下のように、0の重みを定義しておくと、そのオブジェクトとの演算においては、
# RubyStringを自動的にキャストしてくれるので便利である。
a=ZDD::constant(0)
a+="x"
a+="x z"
a+="z"
a.show
EOF
run(scp,title,comment)

