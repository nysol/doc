#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
A,1
B,1
B,2
A,2
B,3
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,name
A,nysol
B,mcmd
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Compute sum on \verb|val| column by \verb|id|.
EOF
scp=<<'EOF'
more dat1.csv
msum i=dat1.csv k=id f=val o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)



############## Example 2
title="Join Process"
comment=<<'EOF'
Use the join key “id” from \verb|dat1.csv|, and join the field “name” from \verb|ref1.csv|.
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mjoin k=id i=dat1.csv m=ref1.csv f=name o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)



