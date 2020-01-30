#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,date
1,20000101
2,20121021
3,
4,19770812
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,time
1,20000101000000
2,20121021111213
3,
4,19770812122212
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='leapyear($d{date})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="時刻型でも判定可能"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mcal c='leapyear($t{time})' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

