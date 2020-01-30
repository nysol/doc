#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("input.csv","w"){|fpw| fpw.write(
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
comment=<<'EOF'
EOF
scp=<<'EOF'
more input.csv
msortf f=顧客 i=input.csv | msum k=顧客 f=金額 o=output.csv
more output.csv
EOF
run(scp,title,comment)

