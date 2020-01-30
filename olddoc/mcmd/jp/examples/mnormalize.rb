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
「顧客」を単位にして「数量」と「金額」項目を基準化（z得点）し、
「数量基準値」と「金額基準値」という項目名で出力する。
EOF
scp=<<'EOF'
more dat1.csv
mnormalize c=z k=顧客 f=数量:数量基準値,金額:金額基準値 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="偏差値"
comment=<<'EOF'
EOF
scp=<<'EOF'
mnormalize c=Z k=顧客 f=数量:数量基準値,金額:金額基準値 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="0から1への線形変換"
comment=<<'EOF'
EOF
scp=<<'EOF'
mnormalize c=range k=顧客 f=数量:数量基準値,金額:金額基準値 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
