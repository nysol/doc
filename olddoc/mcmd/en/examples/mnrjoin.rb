#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
date,price
20080123,10
20080123,20
20080203,10
20080203,35
200804l0,50
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
date,priceF,priceT,avg
20080203,5,15,150
20080203,40,50,200
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
For records where the value of date field is \verb|20080203|, select those records in the input data where \verb|amount| field is more than \verb|5| but less than \verb|15| and join field where \verb|avg=150|. For records where \verb|amount| field is more than \verb|40| but less than \verb|50|, join field \verb|avg=200|.
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mnrjoin k=date f=avg m=ref1.csv R=priceF,priceT r=price%n i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Output unmatched data"
comment=<<'EOF'
Use \verb|-n| to return all records in the input data even if they do not match with those in the reference file (row where \verb|avg=| Null), and use \verb|-N| to return records in the reference file even if they do not match with those in the input file (rows where \verb|price=| null). This is known as outer-join.
EOF
scp=<<'EOF'
mnrjoin k=date f=avg m=ref1.csv R=priceF,priceT r=price%n -n -N i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
