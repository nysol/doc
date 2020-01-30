#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,10
A,,20
B,1,15
B,3,
C,1,20
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,10
A,,
B,1,15
B,3,
C,1,20
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
「数量」と「金額」項目がNULL値の行を削除する。
NULL値の行は\verb|oth.csv|に出力する。
EOF
scp=<<'EOF'
more dat1.csv
mdelnull f=数量,金額 u=oth.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
more oth.csv
EOF
run(scp,title,comment)

############## 例2
title="NULL値の行を選択"
comment=<<'EOF'
\verb|-r|を指定することで、削除ではなく選択することになる。
EOF
scp=<<'EOF'
mdelnull f=数量,金額 -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="キー項目でのNULL値の行の削除"
comment=<<'EOF'
\verb|k=|を指定することで、集計キー単位で削除することになる。
以下では「顧客」項目を単位にして、「数量」と「金額」項目にNULL値が一つでも含まれていれば削除する。
EOF
scp=<<'EOF'
mdelnull k=顧客 f=数量,金額 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="項目間AND条件の例"
comment=<<'EOF'
「数量」と「金額」項目の両方がNULL値の行を削除する。
EOF
scp=<<'EOF'
more dat2.csv
mdelnull f=数量,金額 -F i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="レコード間AND条件の例"
comment=<<'EOF'
「顧客」項目を単位にして、「数量」項目が全てNULL値の行を削除する。
EOF
scp=<<'EOF'
mdelnull k=顧客 f=数量 -R i=dat1.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)
