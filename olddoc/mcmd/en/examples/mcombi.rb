#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,item
A,a1
A,a2
A,a3
B,a4
B,a5
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Enumerate all combinations of two items in the \verb|item| field for each \verb|customer|, and save the output in \verb|item1,item2|.  Fields not specified at \verb|k=,f=| (\verb|item| field in this case) remains after the key field column.
EOF
scp=<<'EOF'
more dat1.csv
mcombi k=customer f=item n=2 a=item1,item2 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Basic Example 2"
comment=<<'EOF'
When you specify the \verb|-dup| option, the output includes combination of the same field.
EOF
scp=<<'EOF'
mcombi k=customer f=item n=2 a=item1,item2 i=dat1.csv o=rsl2.csv -dup
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Compute permutation"
comment=<<'EOF'
Enumerate permutation of two items in the \verb|item| field for each \verb|customer|, and save the output in column \verb|item1,item2|.
EOF
scp=<<'EOF'
mcombi k=customer f=item n=2 a=item1,item2 -p i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
