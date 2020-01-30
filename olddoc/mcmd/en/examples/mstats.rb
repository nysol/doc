#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,quantity,amount
A,1,10
B,5,20
B,2,10
C,1,15
C,3,10
C,1,21
EOF
)}

############## Example 1
title="Basic "
comment=<<'EOF'
Calculate the statistical sum of "quantity" and "amount" field for each "customer".
EOF
scp=<<'EOF'
more dat1.csv
mstats k=customer f=quantity,amount c=sum i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Basic Example 2"
comment=<<'EOF'
Calculate the statistical maximum value.
EOF
scp=<<'EOF'
mstats k=customer f=quantity,amount c=max i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
