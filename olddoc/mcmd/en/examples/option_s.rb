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
After sorting by \verb|id|, calcuate the cumulative sum on \verb|val| column.
EOF
scp=<<'EOF'
more dat1.csv
maccum s=id k=id f=val:val_accum i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)


############## Example 2
title="Specify sort method"
comment=<<'EOF'
After sorting the \verb|val| field in descending numerical order, calculate the cumulative sum on \verb|val| column.
EOF
scp=<<'EOF'
more dat1.csv
maccum s=id,val%nr k=id f=val:val_accum i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)


