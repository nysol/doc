#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,date,quantity
A,20081201,1
A,20081202,2
A,20081203,3
B,20081201,4
B,20081203,5
EOF
)}

############## 例1
title="Example 1: Basic Example"
comment=<<'EOF'
The \verb|item| field is used as the key, and the \verb|date| field is horizontally transposed and the \verb|quantity| field is output.
EOF
scp=<<'EOF'
more dat1.csv
m2cross k=item f=quantity s=date i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="Example 2: Restoring the original input data"
comment=<<'EOF'
The \verb|m2cross| command is used to restore the original input data for the output results of Example 1.
EOF
scp=<<'EOF'
more rsl1.csv
m2cross f=2008* a=date,quantity i=rsl1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="Example 3: Reversing data sequence"
comment=<<'EOF'
The sequence of the horizontally transposed fieldnames is reversed.
EOF
scp=<<'EOF'
m2cross k=item f=quantity s=date%r i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
