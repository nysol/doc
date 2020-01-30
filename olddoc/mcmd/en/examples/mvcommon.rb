#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
items1,items2
b a c,b b
c c,a d
e a a,a a
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
item
a
c
e
EOF
)}


############## Example 1
title="Match common elements in multiple vectors"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mvcommon vf=items1,items2 K=item m=ref1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Print output to a new column"
comment=<<'EOF'
Define new column name for \verb|item2| as \verb|new2|.
EOF
scp=<<'EOF'
mvcommon vf=items1,items2:new2 K=item m=ref1.csv i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
