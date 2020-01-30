#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val1,val2
1,12,36
2,6,5
3,,
4,12.1,36.2
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='gcd(${val1},${val2})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Example of constants"
comment=<<'EOF'
Find out the greatest common divisor of \verb|val1| column and 36.
EOF
scp=<<'EOF'
mcal c='gcd(${val1},36)' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

