#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("input.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,amount
A,5200 
B,4000   
B,3500 
A,2000 
B,800 
EOF
)}

############## Example1
title="Total amount by each customer"
comment=<<'EOF'
EOF
scp=<<'EOF'
more input.csv
msortf f=customer i=input.csv | msum k=customer f=amount o=output.csv
more output.csv
EOF
run(scp,title,comment)

