#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,quantity
A,5
B,10
C,15
D,2
E,50
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Encodes the numeric values in \verb|quantity| column to character strings where values of less than but not equal to 10 are treated as \verb|low|, 10 or more but less than 20 are treated as \verb|middle|, values of 20 or more is treated as \verb|high|.
EOF
scp=<<'EOF'
more dat1.csv
mchgnum f=quantity R=MIN,10,20,MAX v=low,middle,high i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Equal to paramter range"
comment=<<'EOF'
Replace the numeric values in \verb|quantity| column to character strings where 10 or below is treated as \verb|low|, more than 10 but less than or equal to 20 is treated as \verb|middle|, more than 20 is treated as \verb|high|.
EOF
scp=<<'EOF'
mchgnum f=quantity R=MIN,10,20,MAX v=low,middle,high -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
############## Example 3
title="Replace values out of the list of numeric range"
comment=<<'EOF'
Replace numeric values in \verb|quantity| column to character strings  where 10 or above and less than 20 is coded as \verb|low|, 20 or above and less than 30 is coded as \verb|middle|, 30 or more is coded as \verb|high|, values that are less than 10 is coded as \verb|OutOfRange|.
EOF
scp=<<'EOF'
mchgnum f=quantity R=10,20,30,MAX v=low,middle,high O="OutOfRange" i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
############## Example 4
title="Add a new column"
comment=<<'EOF'
Replace the numeric values in \verb|quantity| column to character strings where values less than 10  is treated as \verb|low|, 10 or above but less than 20 is treated as \verb|middle|, 20 or above is treated as \verb|high|. Store the output of replacement strings in a new column as \verb|evaluate|.
EOF
scp=<<'EOF'
mchgnum f=quantity:evaluate R=MIN,10,20,MAX v=low,middle,high -A i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
############## Example 5
title="Display original values in column if out of defined range"
comment=<<'EOF'
Replace the numeric values in \verb|quantity| column to character strings where values of 10 or above but less than 20 is coded as \verb|low|, 20 or above but less than 30 is coded as \verb|middle|, 30 or above is coded as \verb|high|. Retain original values in the output if the value is less than 10.
EOF
scp=<<'EOF'
mchgnum f=quantity R=10,20,30,MAX v=low,middle,high -F i=dat1.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)
