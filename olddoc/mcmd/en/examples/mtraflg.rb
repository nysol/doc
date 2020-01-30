#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,egg,milk
A,1,1
B,,1
C,1,
D,1,1
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Create a string of vector from the list of non-null values in column \verb|egg| and \verb|milk|.
EOF
scp=<<'EOF'
more dat1.csv
mtraflg f=egg,milk a=transaction i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Basic Example 2"
comment=<<'EOF'
Use \verb|-r| option to revert the output results back to the original data.
EOF
scp=<<'EOF'
mtraflg -r f=egg,milk a=transaction i=rsl1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Specify the delimiter"
comment=<<'EOF'
Combine items using the “-” (hyphen) as delimiter. Save output in column named \verb|transaction|.
EOF
scp=<<'EOF'
mtraflg f=egg,milk a=transaction delim=- i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
