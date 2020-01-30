#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
ブランド,数量01,数量02,数量03,数量04,数量05,数量06,数量07,数量08,数量09,数量10
A,10,50,90,130,170,210,250,290,330,370
B,20,60,100,140,180,220,260,300,340,380
C,30,70,110,150,190,230,270,310,350,390
D,40,80,120,160,200,240,280,320,360,400
EOF
)}

############## 例1
title="範囲指定"
comment=<<'EOF'
「0-4」の指定により、「0,1,2,3,4」を指定したことになる。
EOF
scp=<<'EOF'
more dat1.csv
mcut -x f=0-4 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="範囲指定逆順"
comment=<<'EOF'
「4-0」の指定により、「4,3,2,1,0」を指定したことになる。
EOF
scp=<<'EOF'
mcut -x f=4-0 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="複数範囲指定"
comment=<<'EOF'
「1-0,2-4」の指定により、「1,0,2,3,4」を指定したことになる。
EOF
scp=<<'EOF'
mcut -x f=1-0,2-4 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="末尾項目からの指定"
comment=<<'EOF'
「2L」の指定により、項目の後ろから数えた2番項目(数量08)を指定したことになる。
EOF
scp=<<'EOF'
mcut -x f=2L i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="末尾項目からの指定と範囲指定"
comment=<<'EOF'
「5-3L」の指定により、5番項目～後ろから3番目の項目、すなわち「5,6,7」を指定したことになる。
EOF
scp=<<'EOF'
mcut -x f=5-3L i=dat1.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

