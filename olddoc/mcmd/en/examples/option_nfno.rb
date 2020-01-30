#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,10
A,2,20
B,1,15
B,3,10
B,1,20
EOF
)}

############## Example1
title="Basic Example"
comment=<<'EOF'
Extract quantity and amount,but the field names is removed from the output data.
EOF
scp=<<'EOF'
more dat1.csv
mcut -nfno f= quantity, amount i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

