#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example1
title="Customer-based product-quantity matrix"
comment=<<'EOF'
EOF
scp=<<'EOF'
mdata man1 >man1.csv
more man1.csv
mcut f=顧客:customer,日付:date,商品:product i=man1.csv |
mcut f=customer,product o=xxa
more xxa
msortf f=customer,product i=xxa o=xxb
more xxb
# Count the number of rows by customer and product.
mcount k=customer,product a="number of items" i=xxb o=xxc
more xxc
# Perform a cross tabulation by the item of product. The number of the product that is not purchased gives 0.
mcross k=customer s=product f="number of items" v=0 i=xxc o=xxd
more xxd
# remove extra item "fld".
mcut f=fld -r i=xxd o=output.csv
more output.csv
EOF
runfig(scp,title)

