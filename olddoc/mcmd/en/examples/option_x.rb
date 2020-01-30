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

############## Example1
title="Basic Example"
comment=<<'EOF'
Compute the sum of all items in column 1 and 2 of the same key. 
EOF
scp=<<'EOF'
more dat1.csv
msum -x k=0 f=1,2 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Output column names"
comment=<<'EOF'
Rename column 1 and 2 as \verb|a,b| respectively. 
EOF
scp=<<'EOF'
msum -x k=0 f=1:a,2:b i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example3
title="Error when using -nfn"
comment=<<'EOF'
The \verb|-nfn| option assumes data starts from the first row when computing the sum of "quantity" and "amount". However, the result will not be computed as expected since the position of first row of data is defined differently when using \verb|-x| and \verb|-nfn|. 
EOF
scp=<<'EOF'
msum -nfn k=0 f=1,2 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

