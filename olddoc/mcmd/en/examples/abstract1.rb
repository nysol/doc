#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("man0.csv","w"){|fpw| fpw.write(
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
scp=<<'EOF'
msum k=customer f=amount i=man0.csv o=output.csv
more output.csv
EOF
runfig(scp,title)
