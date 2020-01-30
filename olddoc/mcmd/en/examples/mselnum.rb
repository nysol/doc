#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,5.1
2,5
3,-2.0
4,
5,2.0
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Select rows where \verb|val| is greater than 2 and below 5, i.e. records matching \verb|id=2,5| are selected.
EOF
scp=<<'EOF'
more dat1.csv
mselnum f=val c='[2,5]' i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Greater than range"
comment=<<'EOF'
Select rows where \verb|val| is greater than 2, i.e. records where \verb|id=1,2,5|.
EOF
scp=<<'EOF'
mselnum f=val c='[2,]' i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

