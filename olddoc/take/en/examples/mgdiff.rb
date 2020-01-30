#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTexEn.rb"

File.open("g1.csv","w"){|fpw| fpw.write(
<<'EOF'
node1,node2
a,b
b,c
c,d
EOF
)}

File.open("g2.csv","w"){|fpw| fpw.write(
<<'EOF'
node1,node2
b,a
c,d
d,e
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more g1.csv
more g2.csv
mgdiff.rb ei=g1.csv eI=g2.csv o=result1.csv ef=node1,node2
more result1.csv
EOF
run(scp,title,comment)

############## 例2
title="有向グラフとしての比較"
comment=<<'EOF'
EOF
scp=<<'EOF'
 mgdiff.rb ei=g1.csv eI=g2.csv o=result2.csv ef=node1,node2 -dir
 more result2.csv
 EOF 
 run(scp,title,comment)