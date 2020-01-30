#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item1
b a c
c c
e a a
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Replace the default space delimiter to \verb|_|(underscore).
EOF
scp=<<'EOF'
more dat1.csv
mvdelim vf=item1 v=_ i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Comma"
comment=<<'EOF'
In CSV data with comma delimited characters, when the delimiter of vector is replaced as comma, the entire vector is enclosed in double quotes to differentiate from the delimiter of CSV.
EOF
scp=<<'EOF'
mvdelim vf=item1 v=, i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

