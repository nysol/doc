#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Date,Amount
A,20081201,10
A,20081207,20
A,20081213,30
B,20081002,40
B,20081209,50
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Date,Amount
A,20081201,10
A,20081207,20
A,20081213,30
B,20081002,40
B,20081209,50
C,20081210,60
D,20081201,70
D,20081205,80
D,20081209,90
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Randomly select 1 transaction for each customer.
EOF
scp=<<'EOF'
more dat1.csv
mselrand k=Customer c=1 S=1 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Randomly select a percentage of records"
comment=<<'EOF'
Select 50\% of each customers' records at random. Save other records to a separate file \verb|oth.csv|.
EOF
scp=<<'EOF'
mselrand k=Customer p=50 S=1 u=oth2.csv i=dat1.csv o=rsl2.csv
more rsl2.csv
more oth2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Select records by same key"
comment=<<'EOF'
In the following example, select two out of the four customers \verb|A,B,C,D| at random.
Customer \verb|C,D| is selected, and all records of customer \verb|C,D| is printed to the output.

EOF
scp=<<'EOF'
more dat2.csv
mselrand k=Customer c=2 S=1 -B i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
