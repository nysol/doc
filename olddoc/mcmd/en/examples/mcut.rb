#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,quantity,amount
A,1,10
A,2,20
B,1,15
B,3,10
B,1,20
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Extract customer and amount information from the data file \verb|dat1.csv|
Rename the column "amount " to "sales" in the output.
EOF
scp=<<'EOF'
more dat1.csv
mcut f=customer,amount:sales i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Remove columns"
comment=<<'EOF'
Remove columns customer and amount specified at \verb|-r|.
EOF
scp=<<'EOF'
mcut f=customer,amount -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Data without field names"
comment=<<'EOF'
Select columns 0, 2 from an input file without field header, add \verb|customer| and \verb|amount| as field names in the output file.
EOF
scp=<<'EOF'
mcut f=0:customer,2:amount -nfni i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

