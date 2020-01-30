#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,date,price
A,20081201,100
A,20081213,98
B,20081002,400
B,20081209,450
C,20081201,100
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,cost
A,50
B,300
E,200
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Join the field \verb|cost| from the reference file for records where the values of the \verb|item| column from the input file is the same as the values in \verb|item| column in the reference file.
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mjoin k=item f=cost m=ref1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Output unmatched data"
comment=<<'EOF'
Join the \verb|cost| field for records with common key values in the \verb|item| field from the input file and reference file, join \verb|cost| item. At the same time, join all keys from the reference file if the value in the reference file is not in input data range, and set as NULL values.
EOF
scp=<<'EOF'
mjoin k=item f=cost m=ref1.csv -n -N i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
