#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
date,price
20080123,10
20080123,20
20080203,10
20080203,35
200804l0,50
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
date,priceF,priceT,avg
20080203,5,15,150
20080203,40,50,200
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
日付項目の値が\verb|20080203|で、「金額」項目の値が\verb|5|以上\verb|15|未満の入力データ行には\verb|avg=150|を、
\verb|40|以上\verb|50|未満の行には\verb|avg=200|を結合する。
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mnrjoin k=date f=avg m=ref1.csv R=priceF,priceT r=price%n i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="未結合データ出力"
comment=<<'EOF'
\verb|-n|を指定することで、参照ファイルにマッチしない入力ファイルの行(\verb|avg=|がNULL値の行)も出力し、
\verb|-N|を指定することで、入力ファイルにマッチしない参照ファイルの行(\verb|price=|がNULL値の行)も出力する。
いわゆる外部結合である。
EOF
scp=<<'EOF'
mnrjoin k=date f=avg m=ref1.csv R=priceF,priceT r=price%n -n -N i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
