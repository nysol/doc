#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat.csv","w"){|fpw| fpw.write(
<<'EOF'
id
a
b
EOF
)}

File.open("ref.csv","w"){|fpw| fpw.write(
<<'EOF'
id,name
a,A
b,B
EOF
)}


############## Example1
title="Basic Example"
comment=<<'EOF'
If the key size of the reference file is less than 80MB (4MB × 20), the temporary file will not be used.
EOF
scp=<<'EOF'
mnjoin k=id m=ref.csv f=name i=dat.csv o=rsl.csv bufcount=20
EOF
run(scp,title,comment)
