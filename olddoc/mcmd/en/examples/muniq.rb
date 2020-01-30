#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
date,customer
20081201,A
20081202,A
20081202,B
20081202,B
20081203,C
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Remove duplicate records in the \verb|date| field.
EOF
scp=<<'EOF'
more dat1.csv
muniq k=date i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Delete duplicate rows in multiple columns"
comment=<<'EOF'
Remove duplicate records based on unique values in \verb|date| and \verb|customer| field.
EOF
scp=<<'EOF'
muniq k=date,customer i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
