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

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
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
「顧客」と「金額」項目を選択する。ただし、「金額」項目は「売上」と名前を変更して出力している。
EOF
scp=<<'EOF'
more dat1.csv
mcut f=顧客,金額:売上 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="項目削除"
comment=<<'EOF'
\verb|-r|を指定することで、項目を削除できる。
EOF
scp=<<'EOF'
mcut f=顧客,金額 -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="項目名なしデータ"
comment=<<'EOF'
ヘッダなし入力ファイルから、0,2番目の項目を選択し、
「顧客」と「金額」という名前で出力する。
EOF
scp=<<'EOF'
more dat2.csv
mcut f=0:顧客,2:金額 -nfni i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

