#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Quantity,Amount
A,1,5
A,2,20
B,1,15
B,,10
B,5,20
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Calculate the average values of "Quantity" and "Amount" fields for each "Customer", save the computed output in new columns named "AverageVolume" and "AverageAmount".
EOF
scp=<<'EOF'
more dat1.csv
mavg k=Customer f=Quantity:AvgQuantity,Amount:AvgAmount i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Output consisting of NULL values"
comment=<<'EOF'
Calculate the average values of "Quantity" and "Amount" fields for each "Customer", save output in a new columns named "AverageVolume" and "AverageAmount".
When specifying the \verb|-n| option, if a NULL value is included in the input, the result will return NULL value.

EOF
scp=<<'EOF'
mavg k=Customer f=Quantity:AvgQuantity,Amount:AvgAmount -n i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Calculate sum without key field"
comment=<<'EOF'
Calculate the average values of "Quantity" and "Amount" fields, and save the outputs in columns "AvgQuantity" and "AvgAmount".
EOF
scp=<<'EOF'
mavg f=Quantity:AvgQuantity,Amount:AvgAmount i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
