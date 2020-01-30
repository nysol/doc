#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,10
A,2,20
B,1,15
B,3,10
B,1,20
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
0番目項目を集計キーとして1番目と2番目の項目を合計する。
EOF
scp=<<'EOF'
more dat1.csv
msum -x k=0 f=1,2 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="出力項目名も利用可能"
comment=<<'EOF'
1番目と2番目の項目は、\verb|a,b|という名前で出力する。
EOF
scp=<<'EOF'
msum -x k=0 f=1:a,2:b i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="-nfnではうまくいかない"
comment=<<'EOF'
\verb|-nfn|は、最初の行をデータ行としてみなすので、「数量」「金額」というデータを合計しようとしてしまい、うまくいかない。
\verb|-x|は、あくまでも最初の行は項目名行とみなす点が\verb|-nfn|と異なる。
EOF
scp=<<'EOF'
msum -nfn k=0 f=1,2 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

