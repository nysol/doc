#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("man0.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,金額
A,5200 
B,4000   
B,3500 
A,2000 
B,800 
EOF
)}

############## 例1
title="顧客別金額合計"
scp=<<'EOF'
msum k=顧客 f=金額 i=man0.csv o=output.csv
more output.csv
EOF
runfig(scp,title)

