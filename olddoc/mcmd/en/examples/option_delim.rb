#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
vec
b:a:c
x:p
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,vec1,vec2
1,a,b
2,p,q
EOF
)}


############## Example1
title="Basic Example"
comment=<<'EOF'
Sort the elements of the vector field “\verb|vec|” with colon as a delimiter.
EOF
scp=<<'EOF'
more dat1.csv
mvsort vf=vec delim=: i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="When delimiter is not specified"
comment=<<'EOF'
\verb|b:a:c|, \verb|x:p|, etc are intepreted as one element when \verb|delim| is not specified.
EOF
scp=<<'EOF'
mvsort vf=vec i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Use comma as delimiter"
comment=<<'EOF'
If comma is used as delimiter for the vector, the entire vector is enclosed by double quote to draw distinction between the delimiter of CSV and the delimiter of the vector.
EOF
scp=<<'EOF'
more dat2.csv
mvcat vf=vec1,vec2 a=vec3 delim=, i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

