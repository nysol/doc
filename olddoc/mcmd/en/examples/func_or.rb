#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,b1,b2,b3
1,1,0,0
2,1,,1
3,0,,0
4,0,0,0
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='or($b{b1},$b{b2},$b{b3})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Example using wildcard "
comment=<<'EOF'
Use the wildcard character “\verb|b*|” to specify columns starting from \verb|b| (\verb|b1,b2,b3|).
EOF
scp=<<'EOF'
mcal c='or($b{b*})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

