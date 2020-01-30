#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,quantity,amount
A,20,5200 
B,18,4000   
C,15,3500 
D,10,2000 
E,3,800 
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,date,amount
A,20081201,10
A,20081207,20
A,20081213,30
B,20081002,40
B,20081209,50
C,20081003,60
C,20081219,20
EOF
)}

############## 例1 基本例
title="Example 1: Basic example"
comment=<<'EOF'
The input file is partitioned into two, so that the rows are output to the same file as long as the value of the specified field (customer) is the same.
EOF
scp=<<'EOF'
more dat2.csv
mshuffle f=customer d=./dat/d n=2 i=dat2.csv
ls ./dat
more ./dat/d_0
more ./dat/d_1
EOF
system("rm -rf dat")
run(scp,title,comment)


############## 例2 f=を指定しない例
title="Example 2: Not specifying f="
comment=<<'EOF'
The f= parameter is not specified and the input file is partitioned into two. As row number hash values are used, the two files will have almost the same numbers of rows.
EOF
scp=<<'EOF'
more dat2.csv
mshuffle d=./dat/d n=2 i=dat2.csv
ls ./dat
more ./dat/d_0
more ./dat/d_1
EOF
system("rm -rf dat")
run(scp,title,comment)

############## 例3 v=,f=の指定
title="Example 3: Specifying v=,f="
comment=<<'EOF'
With v=2,1 specified, the input file is partitioned into two. Two hash values are allocated to file 0 (d\_0) and one hash value is allocated to file 1 (d\_1).
EOF
scp=<<'EOF'
more dat2.csv
mshuffle f=customer d=./dat/d v=2,1 i=dat2.csv
ls ./dat
more ./dat/d_0
more ./dat/d_1
EOF
system("rm -rf dat")
run(scp,title,comment)

############## 例4 v=の指定
title="Example 4: Specifying v="
comment=<<'EOF'
The script of Example 3 is run without the f= parameter specified. As row number hash values are used, the ratio of the numbers of output rows will be almost the same as the ratio of the weights.
EOF
scp=<<'EOF'
more dat2.csv
mshuffle d=./dat/d v=2,1 i=dat2.csv
ls ./dat
more ./dat/d_0
more ./dat/d_1
EOF
system("rm -rf dat")
run(scp,title,comment)
