#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,b1,b2,b3
1,1,0,1
2,1,1,1
3,1,,1
4,1,1,1
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='and($b{b1},$b{b2},$b{b3})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Example of using wildcard"
comment=<<'EOF'
Specify columns names that start with \verb|b| as in (\verb|b1,b2,b3|) using a wildcard in column name such as "\verb|b*|".
EOF
scp=<<'EOF'
mcal c='and($b{b*})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

