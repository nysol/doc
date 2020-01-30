#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
A,1
B,1
B,2
A,2
B,3
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,name
A,nysol
B,mcmd
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
\verb|id|項目別に\verb|val|項目の値を合計する。
EOF
scp=<<'EOF'
more dat1.csv
msum i=dat1.csv k=id f=val o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
#title="事前に並べ替えない場合"
#comment=<<'EOF'
#項目\verb|id|で並べ変えなければ、キーブレイクが起こる度に集計結果が出力され、期待したように動作しない。
#ただし、この性質を意識して利用することによって集計することはありえる。
#EOF
#scp=<<'EOF'
#msum k=id f=val i=dat1.csv o=rsl2.csv
#more rsl2.csv
#EOF
#run(scp,title,comment)

############## 例3
#title="並べ方は何でもOK"
#comment=<<'EOF'
#逆順に並べても問題ない。
#EOF
#scp=<<'EOF'
#msortf f=id%r i=dat1.csv | msum k=id f=val o=rsl3.csv
#more rsl3.csv
#EOF
#run(scp,title,comment)

############## 例4
title="結合処理"
comment=<<'EOF'
\verb|dat1.csv|の\verb|id|を結合キーに、\verb|ref1.csv|の\verb|name|項目を結合する。
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mjoin i=dat1.csv k=id m=ref1.csv f=name o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
#title="並べ替えない場合"
#comment=<<'EOF'
#並べ替えないと期待通りの結果が得られない。
#以下の結果では、\verb|id=A,val=2|の行が出力されていない。
#EOF
#scp=<<'EOF'
#mjoin k=id m=ref1.csv f=name i=dat1.csv o=rsl5.csv
#more rsl5.csv
#EOF
#run(scp,title,comment)

