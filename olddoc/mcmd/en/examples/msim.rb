#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
x,y,z
14,0.17,-14
11,0.2,-1
32,0.15,-2
13,0.33,-2
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
key,x,y,z
A,14,0.17,-14
A,11,0.2,-1
A,32,0.15,-2
B,13,0.33,-2
B,10,0.8,-5
B,15,0.45,-9
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
x,y,z
1,1,0
1,0,1
1,0,1
0,1,1
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Calculate the cosine and Pearson's product-moment correlation coefficient for the combination of two items among \verb|x, y, z| fields.
EOF
scp=<<'EOF'
more dat1.csv
msim c=pearson,cosine f=x,y,z i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Output diagonal matrix, the upper triangular matrix"
comment=<<'EOF'
Calculate the cosine and Pearson's product-moment correlation coefficient for the combination of two items between \verb|x, y, z|  fields (with d option).
EOF
scp=<<'EOF'
msim c=pearson,cosine f=x,y,z -d i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
############## Example 3
title="Calculation based on key unit"
comment=<<'EOF'
Calculate using \verb|key| field as unit.
EOF
scp=<<'EOF'
more dat2.csv
msim k=key c=pearson,cosine f=x,y,z i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Specify the type of degree of similarity"
comment=<<'EOF'
Using the data with 01 values, compute the phi coefficient and Hamming distance.
EOF
scp=<<'EOF'
more dat3.csv
msim c=hamming,phi f=x,y,z i=dat3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="Rename the column containing degree of similarity"
comment=<<'EOF'
Using the data with 01 values, compute the phi coefficient and Hamming distance and change the output field name.
EOF
scp=<<'EOF'
msim c=hamming:HammingDist,phi:PhiCoeff a=variable1,variable2 f=x,y,z i=dat3.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)
