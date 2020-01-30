#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,date
1,20000101
2,20121021
3,
4,19700101
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,time
1,20000101000000
2,20121021111213
3,
4,19700101000100
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
日付型の\verb|date|項目を\verb|julian|関数でユリウス通日に変換し、\verb|julian2d|関数でまたもとに戻す。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='julian($d{date})' a=julian i=dat1.csv o=rsl1.csv
more rsl1.csv
mcal c='julian2d(${julian})' a=date2 i=rsl1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例2
title="時刻型も同様"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mcal c='julian($t{time})' a=julian i=dat2.csv o=rsl3.csv
more rsl3.csv
mcal c='julian2t(${julian})' a=time2 i=rsl3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

