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
EOF
scp=<<'EOF'
more dat1.csv
mcal c='min(${v1},${v2},${v3})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Example using wildcard"
comment=<<'EOF'
Use wildcard “\verb|v*|” to specify columns starting from \verb|v| (\verb|v1,v2,v3|).
EOF
scp=<<'EOF'
mcal c='min(${v*})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

