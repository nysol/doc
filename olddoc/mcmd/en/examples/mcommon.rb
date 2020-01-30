#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Quantity
A,1
B,2
C,1
D,3
E,1
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Gender
A,Female
B,Male
E,Female
EOF
)}

File.open("ref2.csv","w"){|fpw| fpw.write(
<<'EOF'
CustomerID,Gender
A,Female
B,Male
E,Female
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Quantity 
A,1
A,2
A,3
B,1
D,1
D,2
EOF
)}

File.open("ref3.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer
A
A
D
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Select records with common customers in both input file and reference file. Save unmatched records to a separate file \verb|oth.csv|.
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mcommon k=Customer m=ref1.csv u=oth.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
more oth.csv
EOF
run(scp,title,comment)

############## Example 2
title="Select unmatched records from the input file"
comment=<<'EOF'
Reverse selection criteria by using the \verb|-r| option, the "Customer" not in the reference file are selected.
EOF
scp=<<'EOF'
mcommon k=Customer m=ref1.csv -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Different names of join key"
comment=<<'EOF'
If the join key field name in the reference file is different, specify the field name at ¥verb|K=|.
EOF
scp=<<'EOF'
more ref2.csv
mcommon k=Customer K=CustomerID i=dat1.csv m=ref2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Example with duplicate key fields"
comment=<<'EOF'
Record selection with duplicate records in both input file and reference file.
EOF
scp=<<'EOF'
more dat3.csv
more ref3.csv
mcommon k=Customer m=ref3.csv -r i=dat3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
