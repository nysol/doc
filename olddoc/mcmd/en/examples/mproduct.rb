#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer
A
B
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
date
20090101
20090201
20090301
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Combine the \verb|date| column from reference file to the \verb|customer| column from the input file.
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mproduct f=date m=ref1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
