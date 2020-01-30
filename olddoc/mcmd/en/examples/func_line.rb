#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id
1
2
3
4
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Print number starting from 0 in output.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='line()' a=no i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Start from 1"
comment=<<'EOF'
Print number starting from 1 in output.
EOF
scp=<<'EOF'
mcal c='line()+1' a=no i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

