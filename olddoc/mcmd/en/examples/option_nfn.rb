#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
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
Extract column0 and 2.
EOF
scp=<<'EOF'
more dat1.csv
mcut -nfn f=0,2 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

