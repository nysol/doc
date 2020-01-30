#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,3.141592
2,-1.047197
3,
4,6.283185
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='cosh(${val})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
