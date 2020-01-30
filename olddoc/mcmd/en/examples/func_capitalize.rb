#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,abc
2,aBd
3,
4,#abc
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Convert the first character of $str$ field to uppercase.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='capitalize($s{str})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

