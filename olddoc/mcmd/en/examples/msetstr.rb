#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,date
A,20081202
A,20081204
B,20081203
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Calculate the date by setting a reference date  (defined as January 01, 2007)  and add the string “\verb|20070101|” in all lines and save the output as a new column named “ReferenceDate”.
EOF
scp=<<'EOF'
more dat1.csv
msetstr v=20070101 a=ReferenceDate i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Add multiple fields"
comment=<<'EOF'
EOF
scp=<<'EOF'
msetstr v=20070101,20070201 a=RefDate1,RefDate2 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Add column with null values"
comment=<<'EOF'
EOF
scp=<<'EOF'
msetstr v= a=NewColumn i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
