#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,b
1,1
2,
3,0
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='not($b{b})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
