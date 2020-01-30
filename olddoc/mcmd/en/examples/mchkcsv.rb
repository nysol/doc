#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
product,date,quantity,amount
A,20081201,1,10
A,20081202,2,
A,*,3
B,20081201,4,40
B,20081203,50
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
fld1,fld2,fld3,fld4
A,20081201,1,10
A,20081202,2,
A,*,3
B,20081201,4,40
B,20081203,50
EOF
)}


############## Example 1
title="Repair data"
comment=<<'EOF'
This data contains different number of columns in all records. For instance, only 3 records have 4 columns. Use M-Command to repair and standardize 3rd and 5th rows to 4 columns.
EOF
scp=<<'EOF'
more dat1.csv
mchkcsv i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Change field name after repairing the data"
comment=<<'EOF'
This data contains different number of columns in all records. For instance, only 3 records have 4 columns. Use M Command to repair and standardize 3rd and 5th rows to 4 columns. At the same time, label the field names from the input data as ¥verb|“product,date,quantity,amount”| starting from the left.
EOF
scp=<<'EOF'
more dat2.csv
mchkcsv a=product,date,quantity,amount i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Check data integrity and output diagnostic results"
comment=<<'EOF'
It merely checks for incomplete data structure in the CSV data, and save the diagnosis result in CSV file.
EOF
scp=<<'EOF'
mchkcsv -diag i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
