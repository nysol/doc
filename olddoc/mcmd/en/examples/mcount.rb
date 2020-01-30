#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
date
20090109
20090109
20090109
20090110
20090110
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Count the number of rows by date, and save the results in a new column \verb|count|.
EOF
scp=<<'EOF'
more dat1.csv
mcount k=date a=count i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Count without aggregate key"
comment=<<'EOF'
Count the number of rows without specifying the aggregate key.
EOF
scp=<<'EOF'
mcount a=count i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

