#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="パイプで連結した例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mdata -man1 | mcut f=顧客,商品 | mcount k=顧客,商品 a=件数 | mcross k=顧客 s=商品 f=件数 v=0 | mcut f=fld -r o=output.csv
more output.csv
EOF
runfig(scp,title)

