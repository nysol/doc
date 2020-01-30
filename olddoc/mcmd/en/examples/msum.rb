#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,quantity,amount
A,1,10
A,2,20
B,1,15
B,3,10
B,1,20
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Calculate the total value of "quantity" and "amount" for each "customer".  Save the output with field names "total quantity" and "total amount".
EOF
scp=<<'EOF'
more dat1.csv
msum k=customer f=quantity:quantitySum,amount:amountSum i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
