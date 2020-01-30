#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
日付,金額
20080123,10
20080203,10
20080203,20
20080203,45
200804l0,50
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
日付,金額F,金額T
20080203,5,15
20080203,40,50
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
日付項目の値が\verb|20080203|で、「金額」項目の値が\verb|5|以上\verb|15|未満の行、および\verb|40|以上\verb|50|未満の行を選択する。
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mnrcommon k=日付 m=ref1.csv R=金額F,金額T r=金額%n i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="条件反転"
comment=<<'EOF'
\verb|-r|を付けると選択条件は反転する。
EOF
scp=<<'EOF'
mnrcommon k=日付 m=ref1.csv R=金額F,金額T r=金額%n -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
