#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
gender,visitgap,purchasepattern,hospitalized
Male,1.2,ABCAAA,Yes
Male,10.5,BCDADD,Yes
Male,0.5,AAAA,No
Male,2.0,BBCC,No
Male,3.1,DEDDA,Yes
Female,0.7,CCCAA,No
Female,1.5,DDDEEE,Yes
Female,2.6,BACD,Yes
Female,3.5,ABBB,Yes
Female,4.0,DDDD,Yes
Female,2.1,DEDE,No
Male,1.2,ABCAAA,Yes
Male,10.5,BCDADD,Yes
Male,0.5,AAAA,No
Male,2.0,BBCC,No
Male,3.1,DEDDA,Yes
Male,0.7,CCCAA,No
Male,1.5,DDDEEE,No
Male,2.6,BACD,Yes
Male,3.5,ABBB,Yes
Male,4.0,DDDD,Yes
Male,2.1,DEDE,No
Male,1.2,ABCAAA,Yes
Male,10.5,BCDADDA,Yes
Male,0.5,AAAAA,No
Male,2.0,BBCCA,No
Male,3.1,DEDDA,Yes
Male,0.7,CCCAA,No
Male,1.5,ADDDEEE,Yes
Male,2.6,BACD,Yes
Male,3.5,ABBB,Yes
Male,4.0,DDDD,Yes
Female,2.1,DEDE,No
Female,1.2,ABCAAA,Yes
Female,10.5,BCDADD,Yes
Female,0.5,AAAA,No
Female,2.0,BBCC,No
Female,3.1,DEDDA,Yes
Female,0.7,CCCAA,No
Female,1.5,DDDEEE,Yes
Female,2.6,BACD,Yes
Female,3.5,ABBB,Yes
Female,4.0,DDDD,Yes
Female,2.1,DEDE,No
Female,1.2,ABCAAA,Yes
Female,10.5,BCDADD,Yes
Female,0.5,AAAA,No
Female,2.0,BBCC,No
Female,3.1,DEDDA,Yes
Female,0.7,CCCAA,No
Female,1.5,DDDEEE,Yes
Female,2.6,BACD,Yes
Female,3.5,ABBB,Yes
Female,1.0,DDDD,Yes
Female,2.5,DEDE,No
Female,2.5,ABBB,Yes
Female,1.0,DDDD,Yes
Female,1.1,DEDE,No
Female,2.2,ABCAAA,Yes
Female,10.5,BCDADD,Yes
Female,1.5,AAAA,No
Female,2.6,BBCC,No
Female,3.3,DEDDA,Yes
Female,1.7,CCCAA,No
Female,1.5,DDDEEE,Yes
Female,2.6,BACD,Yes
Female,3.9,ABBB,Yes
Female,4.5,DDDD,Yes
Female,2.1,DEDE,No
Female,3.9,BABB,Yes
Male,4.5,BAA,No
Female,2.1,DEDE,No
Male,3.9,BABB,Yes
Female,3.9,BABB,Yes
Male,4.5,BAA,No
Female,2.1,DEDE,No
Male,3.9,BABB,Yes
Female,3.9,BABB,Yes
Male,4.5,BAA,No
Female,2.1,DEDE,No
Male,3.9,BABB,Yes
EOF
)}

############## 例1
title="Basic Example"
comment=<<'EOF'
Example from the above section.
EOF
scp=<<'EOF'
cat dat1.csv
mbonsai c=hospitalized n=visitgap p=purchasepattern d=gender i=dat1.csv O=outdat
mdtree.rb i=outdat/model.pmml o=model1.html
mdtree.rb alpha=0.1 i=outdat/model.pmml o=model2.html
head model1.html
head model2.html
EOF
run(scp,title,comment)

