#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
node1,node2,val
a,b,1
a,c,2
a,d,1
b,c,3
b,d,3
c,f,1
c,e,4
d,e,1
e,f,3
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
前節の解説で用いてる例。
EOF
scp=<<'EOF'
more dat1.csv
msankey.rb i=dat1.csv f=node1,node2 v=val o=output.html
head output.html
EOF
run(scp,title,comment)

