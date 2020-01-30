#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,v1,v2,v3
1,1,2,3
2,-5,2,1
3,1,,3
4,,,
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Count the number of column names that start with \verb|"v"|.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='argsize($s{v*})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

