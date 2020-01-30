#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,time
1,20000101000000
2,20121021111213
3,
4,19770812122212
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='second($t{time})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Return character string"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='seconds($t{time})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

