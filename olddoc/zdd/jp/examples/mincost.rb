#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
\hyperref[sect:maxcover]{maxcover}メソッドの例を参照のこと。
EOF
scp=<<'EOF'
EOF
run(scp,title,comment)

