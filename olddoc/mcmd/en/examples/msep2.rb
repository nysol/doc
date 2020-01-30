#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,no
A,1
A,1
A,2
B,1
B,2
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Split the data by corresponding values in \verb|item| field. Output file names are sequential numbers starting from 0. The key and corresponding number is printed to \verb|table.csv|.
EOF
scp=<<'EOF'
more dat1.csv
msep2 k=item O=./output a=fileName o=table.csv i=dat1.csv
ls ./output
more table.csv
more output/0
more output/1
EOF
run(scp,title,comment)

############## Example 2
title="Multiple key fields"
comment=<<'EOF'
Each file name is created according to the sequential number using \verb|item,no| as the composite key field. The key field and its corresponding sequential file names are printed to \verb|table.csv|.
EOF
scp=<<'EOF'
more dat1.csv
msep2 k=item,no O=./output2 a=fileName o=table.csv i=dat1.csv
ls ./output2
more table.csv
more output/0
EOF
run(scp,title,comment)
