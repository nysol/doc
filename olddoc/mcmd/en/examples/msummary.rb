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
Find out the median and average "quantity" and "amount" by each customer.
Save the output in a new column named "type".
EOF
scp=<<'EOF'
more dat1.csv
msummary k=customer f=quantity,amount c=median:medianval,mean:meanval a=type i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)