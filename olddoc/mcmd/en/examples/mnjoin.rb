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
A,70
B,300
E,200
EOF
)}

File.open("ref2.csv","w"){|fpw| fpw.write(
<<'EOF'
item,cost
A,50
B,300
E,200
EOF
)}

############## Example 1
title="Basic Example "
comment=<<'EOF'
The \verb|item| field in the input file is compared with the \verb|item| field from the reference file, add \verb|cost| field for records with the same value. There are two records where \verb|item=A| in both input file and reference file, therefore, 2$\times$2=4 rows of \verb|item=A| is written to the output file.
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mnjoin k=item f=cost m=ref1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Ouput unmatched data"
comment=<<'EOF'
Use \verb|-n| to print records in the input data that do not match with those in the reference file (row where \verb|item="C"|), and use -N to print records in the reference file that do not match with those in the input file (row where \verb|item="E"|).
EOF
scp=<<'EOF'
more ref2.csv
mnjoin k=item f=cost m=ref2.csv -n -N i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
