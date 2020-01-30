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
Example shown in the previous section. 
EOF
scp=<<'EOF'
more clique.csv
mclique2g.rb i=clique.csv eo=edge.csv no=node.csv id=id f=node
more edge.csv
more node.csv
EOF
run(scp,title,comment)

