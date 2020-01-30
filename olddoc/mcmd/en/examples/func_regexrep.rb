#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,caabaa
2,acabaaa
3,
4,cbcbcc
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
In row where \verb|id=1,id=2|, the matched substrings in the column is replaced with \verb|MMM|.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexrep($s{str},"c.*aa","MMM")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

