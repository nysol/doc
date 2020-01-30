#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Quantity,Amount
A,20,5200 
B,18,4000   
C,15,3500 
D,10,2000 
E,3,800 
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
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
This example assumed that the "quantity" and "amount" fields are sorted from the largest value (descending order).
Records are selected from the first row (line 0) by default if \verb|from=|,\verb|to=|,\verb|size=| parameters are not specified.
EOF
scp=<<'EOF'
more dat1.csv
mbest s=Quantity%nr,Amount%nr i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Basic Example 2"
comment=<<'EOF'
After sorting by "customers", select 3 rows from the first row (line 0).
EOF
scp=<<'EOF'
mbest s=Customer from=0 size=3 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Basic Example 3"
comment=<<'EOF'
Without sorting (in the original order), select from line 0 to line 1.
EOF
scp=<<'EOF'
mbest -q from=0 to=1 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Reverse Selection"
comment=<<'EOF'
Select records other than customers' first visit to store.
Save the records of customers' first visit to the file \verb|fvd.csv|.
EOF
scp=<<'EOF'
more dat2.csv
mbest s=Customer,Date k=Customer -r u=fvd.csv i=dat2.csv o=rsl4.csv
more rsl4.csv
more fvd.csv
EOF
run(scp,title,comment)
