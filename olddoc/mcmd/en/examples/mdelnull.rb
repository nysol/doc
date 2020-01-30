#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Quantity,Amount
A,1,10
A,,20
B,1,15
B,3,
C,1,20
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Quantity,Amount
A,1,10
A,,
B,1,15
B,3,
C,1,20
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Remove records where \verb|Quantity| and \verb|Amount| contain null values. Save records with null values to a separate file \verb|oth.csv|.
EOF
scp=<<'EOF'
more dat1.csv
mdelnull f=Quantity,Amount u=oth.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
more oth.csv
EOF
run(scp,title,comment)

############## Example 2
title="Select rows with NULL values"
comment=<<'EOF'
Select records with NULL values by specifying \verb|-r|.
EOF
scp=<<'EOF'
mdelnull f=Quantity,Amount -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Remove records with the same key if any record contains NULL values"
comment=<<'EOF'
Remove based on the aggregate key specified at \verb|k=|.
Remove records where \verb|Quantity| and \verb|Amount| contain null values for each customer.
EOF
scp=<<'EOF'
mdelnull k=Customer f=Quantity,Amount i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="AND condition between fields"
comment=<<'EOF'
Remove the record where both \verb|Quantity| and \verb|Amount| fields contain null values.
EOF
scp=<<'EOF'
more dat2.csv
mdelnull f=Quantity,Amount -F i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="AND condition between records"
comment=<<'EOF'
Remove the \verb|Customer| record if all values in \verb|Quantity| is NULL.
EOF
scp=<<'EOF'
mdelnull k=Customer f=Quantity -R i=dat1.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)
