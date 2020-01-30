#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,10
A,2,20
B,1,30
B,3,40
B,1,50
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
a,b
A,-1
B,
C,1
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
「金額」項目の値が40より大きい行を選択する。
それ以外のデータは\verb|unmatch1.csv|に出力する。
EOF
scp=<<'EOF'
more dat1.csv
msel c='${金額}>40' u=unmatch1.csv i=dat1.csv o=match1.csv
more match1.csv
more unmatch1.csv
EOF
run(scp,title,comment)

############## 例2
title="NULL値の選択規制"
comment=<<'EOF'
\verb|msel|コマンドでは\verb|c=|で与えられた式を評価した結果がNULL値の場合その行は選択されない。
また、アンマッチ出力ファイルが\verb|u=|によって指定されていれば、そのファイルに出力される。
以下の例では項目\verb|b|に\verb|-1|、NULL値、\verb|1|を持つ3行のデータについて、0より大きい行を選択しているが、
NULL値を含む行はアンマッチ出力ファイルへと出力される。
EOF
scp=<<'EOF'
more dat2.csv
msel c='${b}>0' i=dat2.csv o=match2.csv u=unmatch2.csv
more match2.csv
more unmatch2.csv
EOF
run(scp,title,comment)

############## 例3
title="-rオプション指定"
comment=<<'EOF'
真偽は逆転するがNULL値の評価に変わりはない。
すなわちNULL値の行は選択されない。
以下の例では、上の例と同様のデータおよび選択条件で\verb|-r|をつけている。
真偽の選択条件は逆転しているが、NULL値を含む行は上記の例と同様にアンマッチファイルへと出力されていることがわかる。
EOF
scp=<<'EOF'
msel -r c='${b}>0' i=dat2.csv o=match3.csv u=unmatch3.csv
more match3.csv
more unmatch3.csv
EOF
run(scp,title,comment)
