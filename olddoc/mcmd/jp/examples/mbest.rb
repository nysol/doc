#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,20,5200 
B,18,4000   
C,15,3500 
D,10,2000 
E,3,800 
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,日付,金額
A,20081201,10
A,20081207,20
A,20081213,30
B,20081002,40
B,20081209,50
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
この例では、「数量」と「金額」項目値の大きい順（降順）に並べ替えている。
\verb|from=|,\verb|to=|,\verb|size=|を指定しなければ先頭行(0行目)のみ選択する
EOF
scp=<<'EOF'
more dat1.csv
mbest s=数量%nr,金額%nr i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="基本例2"
comment=<<'EOF'
「顧客」で並べ替えた後、先頭行(0行目)から3行選択する
EOF
scp=<<'EOF'
mbest s=顧客 from=0 size=3 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="基本例3"
comment=<<'EOF'
並べ替えを行わず(もとのレコード順序を維持したまま)、0行目から1行目まで選択する
EOF
scp=<<'EOF'
mbest -q from=0 to=1 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="条件反転"
comment=<<'EOF'
顧客の初回来店日以外の行を選択する。
初回来店日は\verb|fvd.csv|というファイルに出力する。
EOF
scp=<<'EOF'
more dat2.csv
mbest s=顧客,日付 k=顧客 -r u=fvd.csv i=dat2.csv o=rsl4.csv
more rsl4.csv
more fvd.csv
EOF
run(scp,title,comment)
