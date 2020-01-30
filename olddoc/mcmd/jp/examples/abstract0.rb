#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="mdataコマンドによるデータの生成"
scp=<<'EOF'
mdata -man0 >man0.csv
more man0.csv
EOF
runfig(scp,title)

