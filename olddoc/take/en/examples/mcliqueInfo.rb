#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTex.rb"

File.open("clique.csv","w"){|fpw| fpw.write(
<<'EOF'
id,node
0,a
0,b
0,c
0,d
1,d
1,e
1,f
2,e
2,f
2,g
3,e
3,f
3,h
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Example illustrated in the previous section.
EOF
scp=<<'EOF'
more clique.csv
mcliqueInfo.rb i=clique.csv o=result1.csv id=id f=node
more result1.csv
EOF
run(scp,title,comment)


