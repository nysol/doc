#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTex.rb"

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

############## 例1
title="基本例"
comment=<<'EOF'
前節の解説で用いてる例。
EOF
scp=<<'EOF'
more dat1.csv
mclique.rb ei=dat1.csv ef=node1,node2 o=result1.csv log=log1.csv
more result1.csv
more cn1.csv
more ce1.csv
more log1.csv
EOF
run(scp,title,comment)

############## 例2
title="サイズが4以上の極大クリークのみ列挙"
comment=<<'EOF'
EOF
scp=<<'EOF'
mclique.rb ei=dat1.csv ef=node1,node2 l=4 o=result2.csv
more result2.csv
EOF
run(scp,title,comment)

############## 例3
title="サイズが3の全クリークを列挙"
comment=<<'EOF'
EOF
scp=<<'EOF'
mclique.rb ei=dat1.csv ef=node1,node2 l=3 u=3 -all o=result3.csv
more result3.csv
EOF
run(scp,title,comment)


