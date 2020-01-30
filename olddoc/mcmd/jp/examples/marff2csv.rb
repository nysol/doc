#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.arff","w"){|fpw| fpw.write(
<<'EOF'
@RELATION       顧客購買データ

@ATTRIBUTE      顧客    string
@ATTRIBUTE      日付    date yyyyMMdd
@ATTRIBUTE      数量    numeric
@ATTRIBUTE      金額    numeric
@ATTRIBUTE      商品    {A,B}

@DATA
No.1,20081201,1,10,A
No.2,20081202,2,20,A
No.3,20081203,3,30,A
No.4,20081201,4,40,B
No.5,20081203,5,50,B
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
arff形式の顧客購買データをcsv形式のデータへ変換する。
EOF
scp=<<'EOF'
more dat1.arff
marff2csv i=dat1.arff  o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

