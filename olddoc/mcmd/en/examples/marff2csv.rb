#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.arff","w"){|fpw| fpw.write(
<<'EOF'
@RELATION       Customer Purchase Data

@ATTRIBUTE      Customer    string
@ATTRIBUTE      Date    date yyyymmdd
@ATTRIBUTE      Quantity    numeric
@ATTRIBUTE      Amount    numeric
@ATTRIBUTE      Product    {A,B}

@DATA
No.1,20081201,1,10,A
No.2,20081202,2,20,A
No.3,20081203,3,30,A
No.4,20081201,4,40,B
No.5,20081203,5,50,B
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Convert customer purchasing data in arff format to csv format. 
EOF
scp=<<'EOF'
more dat1.arff
marff2csv i=dat1.arff  o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

