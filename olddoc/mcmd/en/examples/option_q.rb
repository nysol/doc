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

############## Example 1
title="Basic Example "
comment=<<'EOF'
Find out the cumulative value by \verb|id| field. When \verb|-q| option is specified, sorting by field specified at \verb|k=| parameter will be disabled.
EOF
scp=<<'EOF'
more dat1.csv
maccum -q k=id f=val:val_accum i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

