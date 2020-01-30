#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
商品,日付,数量,金額
A,20081201,1,10
A,20081202,2,
A,*,3
B,20081201,4,40
B,20081203,50
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
fld1,fld2,fld3,fld4
A,20081201,1,10
A,20081202,2,
A,*,3
B,20081201,4,40
B,20081203,50
EOF
)}


############## 例1
title="データの補完"
comment=<<'EOF'
データの項目数が違う（2,4行目が3項目しかない）問題のあるデータを
Mコマンドで利用できるデータに補完（4項目に自動的に補完）する。
EOF
scp=<<'EOF'
more dat1.csv
mchkcsv i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="データの補完、項目名変更"
comment=<<'EOF'
データの項目数が違う（3,5行目が3項目しかない）問題のあるデータを
Mコマンドで利用できるデータに補完（4項目に自動的に補完）する。
その際に、入力データの左の項目から順番に「\verb|商品,日付,数量,金額|」という項目名で出力する。
EOF
scp=<<'EOF'
more dat2.csv
mchkcsv a=商品,日付,数量,金額 i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="データの不備チェック、診断結果の出力"
comment=<<'EOF'
CSVデータに不備な箇所がないかチェックのみを行い、CSVファイル診断結果を出力する。
EOF
scp=<<'EOF'
mchkcsv -diagl i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
