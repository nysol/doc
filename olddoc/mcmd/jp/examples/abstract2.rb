#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="顧客別商品購入数量マトリックス"
comment=<<'EOF'
EOF
scp=<<'EOF'
mdata -man1 >man1.csv
more man1.csv
mcut f=顧客,商品 i=man1.csv o=xxa
more xxa
# 顧客商品別に行数をカウントする。
mcount k=顧客,商品 a=件数 i=xxa o=xxb
more xxb
# 商品を項目にしたクロス集計を実行。購入されていない商品の個数は0にしている。
mcross k=顧客 s=商品 f=件数 v=0 i=xxb o=xxc
more xxc
# 余分な項目"fld"を除いている。
mcut f=fld -r i=xxc o=output.csv
more output.csv
EOF
runfig(scp,title)

