#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTex.rb"

File.open("dat.csv","w"){|fpw| fpw.write(
<<'EOF'
node1,node2
a,A
a,B
a,C
b,A
b,B
b,D
c,A
c,D
d,B
d,C
d,D
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
前節の解説で用いてる例。
EOF
scp=<<'EOF'
more dat.csv
mbiclique.rb ei=dat.csv ef=node1,node2 o=result1.csv
more result1.csv
EOF
run(scp,title,comment)

############## 例2
title="サイズを制限する例"
comment=<<'EOF'
項目\verb|node1,node2|共にサイズが2の極大二部クリークを列挙する。
EOF
scp=<<'EOF'
mbiclique.rb ei=dat.csv ef=node1,node2 o=result2.csv l=2,2 u=2,2
more result2.csv
EOF
run(scp,title,comment)

############## 例2
title="部分的にサイズを制限する例"
comment=<<'EOF'
項目\verb|node1|のサイズの下限を1に(デフォルトの下限が1なので実際には意味がないが指定例として)、
項目\verb|node2|のサイズの上限を3に制限した極大二部クリークを列挙する。
\verb|u=|パラメータの1番目の値がnullになっているのは、項目\verb|node1|の上限を設定しなためである。

EOF
scp=<<'EOF'
mbiclique.rb ei=dat.csv ef=node1,node2 o=result3.csv l=1, u=,3
more result3.csv
EOF
run(scp,title,comment)

