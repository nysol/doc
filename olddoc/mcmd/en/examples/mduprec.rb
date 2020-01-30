#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
store,val
A,2
B,
C,5
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Generate multiple records of the data based on the numeric value in the “Quantity” field. Records containing NULL values will not be duplicated.
EOF
scp=<<'EOF'
more dat1.csv
mduprec f=val i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Define the number of rows to duplicate"
comment=<<'EOF'
Duplicate two rows (\verb|n=2|) for each record in the dataset.
EOF
scp=<<'EOF'
mduprec n=2 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
