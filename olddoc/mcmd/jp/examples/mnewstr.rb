#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
\verb|custNo|と\verb|A0001|という文字列データを5行作成し、\verb|attribute,code|という名前の項目名で出力する。
EOF
scp=<<'EOF'
mnewstr a=attribute,code v=custNo,A0001 l=5 o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
