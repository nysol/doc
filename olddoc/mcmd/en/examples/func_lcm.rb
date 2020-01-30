#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val1,val2
1,5,3
2,12,4
3,,
4,5.1,3.1
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='lcm(${val1},${val2})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Example using constant"
comment=<<'EOF'
Find out the least common denominator between column \verb|val1| and 15.
EOF
scp=<<'EOF'
mcal c='lcm(${val1},15)' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

