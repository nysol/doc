#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,date,quantity,price
A,20081201,1,10
B,20081201,4,40
A,20081202,2,20
A,20081203,3,30
B,20081203,5,50
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Create a directory named \verb|dat|, and separate the data according to the \verb|date| value in the directory.
EOF
scp=<<'EOF'
more dat1.csv
msep d='./dat/${date}.csv' -p i=dat1.csv
ls ./dat
more ./dat/20081201.csv
more ./dat/20081202.csv
more ./dat/20081203.csv
more ./dat/B.csv
EOF
system("rm -rf dat")
run(scp,title,comment)

############## Example 2
#title="Error if data is not sorted"
#comment=<<'EOF'
#The command will not work properly if \verb|item| field is not sorted beforehand.
#EOF
#scp=<<'EOF'
#msep d='./dat/${item}.csv' -p i=dat1.csv
#ls ./dat
#more ./dat/A.csv
#more ./dat/B.csv
#EOF
#system("rm -rf dat")
#run(scp,title,comment)
