#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,product,date,quantity,amount
No.1,A,20081201,1,10
No.2,A,20081202,2,20
No.3,A,20081203,3,30
No.4,B,20081201,4,40
No.5,B,20081203,5,50
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,product,date,quantity,amount
No.1,A,20081201102030,1,10
No.2,A,20081202123010,2,20
No.3,A,20081203153010,3,30
No.4,B,20081201174010,4,40
No.5,B,20081203133010,5,50
EOF
)}


############## Example 1
title="Convert csv format data to arff format"
comment=<<'EOF'
Convert data to arff format and define "customer" field as string type, "product" field as category type, "date" field as date type (exclude time), “quantity” and “amount” fields as numeric attributes.
EOF
scp=<<'EOF'
more dat1.csv
mcsv2arff s=customer d=product D=date n=quantity,amount T=Purchase_Data i=dat1.csv  o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Convert csv format data to arff format (include time in the date attribute)"
comment=<<'EOF'
Specify the date with the time information by adding \verb|%t| such that \verb|D=date%t|.
EOF
scp=<<'EOF'
more dat2.csv
mcsv2arff s=customer d=product D=date%t n=quantity,amount T=Purchase_Data i=dat2.csv  o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
