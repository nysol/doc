#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Quantity,Amount
A,1,10
A,2,20
B,1,15
B,3,10
B,1,20
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Quantity,Amount
A,1,10
A,,20
B,1,15
B,3,
B,1,20
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Calculate the cumulative values ​​of "Quantity" and "Amount" fields for each "Customer", save output as new data attributes in new columns named "AccumQuantity" and "AccumlAmount".
EOF
scp=<<'EOF'
more dat1.csv
maccum s=Customer f=Quantity:AccumQuantity,Amount:AccumAmount i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Specify Calculation by Key"
comment=<<'EOF'
Calculates the cumulative value of "Quantity" and "Amount" fields for each "Customer", and save the output in new columns named "AccumQuantity" and  "AccumAmount".
EOF
scp=<<'EOF'
more dat1.csv
maccum k=Customer s=Customer f=Quantity:AccumQuantity,Amount:AccumAmount i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Cumulative computation with NULL values"
comment=<<'EOF'
Calculate the cumulative values ​​of "Quantity" and "Amount" item, and save the output as new columns named "AccumQuantity" and "AccumAmount". NULL values are ignored. Records with NULL values will be retained in the output.
EOF
scp=<<'EOF'
more dat2.csv
maccum s=Customer f=Quantity:AccumQuantity,Amount:AccumAmount i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
