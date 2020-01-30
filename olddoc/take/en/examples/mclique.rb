#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTexEn.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
node1,node2
a,b
a,c
a,d
a,e
b,c
b,d
b,f
c,d
c,e
d,e
e,f
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Example illustrated from the above section.
EOF
scp=<<'EOF'
more dat1.csv
mclique.rb i=dat1.csv f=node1,node2 o=result1.csv log=log1.csv
more result1.csv
more cn1.csv
more ce1.csv
more log1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Enumerate maximal cliques with size 4 or above"
comment=<<'EOF'
EOF
scp=<<'EOF'
mclique.rb i=dat1.csv f=node1,node2 l=4 o=result2.csv
more result2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Enumerate all cliques with size of 3"
comment=<<'EOF'
EOF
scp=<<'EOF'
mclique.rb i=dat1.csv f=node1,node2 l=3 u=3 -all o=result3.csv
more result3.csv
EOF
run(scp,title,comment)


