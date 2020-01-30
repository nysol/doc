#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
items
b a  c
 c c
e a   b 
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
items
b.a..c
.c.c
e.a...b.
EOF
)}


############## Example1
title="Example 1: Basic example of removing null characters"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mvdelnull vf=items i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Example 2: Example of using .(dot) as delimiting character"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mvdelnull vf=items delim=. i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example3
title="Example 3: Change field name and output "
comment=<<'EOF'
EOF
scp=<<'EOF'
mvdelnull vf=items:new i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example4
title="Example 3: Add output as an new field by specifying -A"
comment=<<'EOF'
EOF
scp=<<'EOF'
mvdelnull vf=items:new -A i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
