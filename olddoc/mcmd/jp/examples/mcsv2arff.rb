#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,商品,日付,数量,金額
No.1,A,20081201,1,10
No.2,A,20081202,2,20
No.3,A,20081203,3,30
No.4,B,20081201,4,40
No.5,B,20081203,5,50
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,商品,日付,数量,金額
No.1,A,20081201102030,1,10
No.2,A,20081202123010,2,20
No.3,A,20081203153010,3,30
No.4,B,20081201174010,4,40
No.5,B,20081203133010,5,50
EOF
)}


############## 例1
title="csv形式のデータをarff形式のデータへ変換"
comment=<<'EOF'
「顧客」項目は文字列型、
「商品」項目はカテゴリ型、
「日付」項目は日付型(時刻は含まない)、
そして「数量」と「金額」項目は数値型として、
arff形式のデータへ変換する。
EOF
scp=<<'EOF'
more dat1.csv
mcsv2arff s=顧客 d=商品 D=日付 n=数量,金額 T=顧客購買データ i=dat1.csv  o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="csv形式のデータをarff形式のデータへ変換(時刻を含む日付データ指定)"
comment=<<'EOF'
時刻を伴うデータは\verb|D=日付%t|のように\verb|%t|を加えて指定する。
EOF
scp=<<'EOF'
more dat2.csv
mcsv2arff s=顧客 d=商品 D=日付%t n=数量,金額 T=顧客購買データ i=dat2.csv  o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
