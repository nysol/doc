#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id
A
B
C
EOF
)}

############## Example1
title="Basic Example"
comment=<<'EOF'
Add a new field as “payday”.
EOF
scp=<<'EOF'
more dat1.csv
msetstr v=20070101 a=payday i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Add multiple fields"
comment=<<'EOF'
Enumerate the two combination of each item \verb|A,B,C| in the column “id”.
EOF
scp=<<'EOF'
mcombi f=id n=2 a=id1,id2 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

