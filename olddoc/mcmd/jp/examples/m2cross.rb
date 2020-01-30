#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,date,quantity
A,20081201,1
A,20081202,2
A,20081203,3
B,20081201,4
B,20081203,5
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
item,week,quantity
A,Monday,1
A,Tuesday,2
A,Wednesday,3
B,Thursday,4
B,Friday,5
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
\verb|item|項目を単位に\verb|date|項目を横に展開し、
\verb|quantity|項目を出力する。
EOF
scp=<<'EOF'
more dat1.csv
m2cross k=item f=quantity s=date i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="元の入力データに戻す例"
comment=<<'EOF'
例1の出力結果を元に戻すには、同じく\verb|m2cross|を以下のよう用いればよい。
EOF
scp=<<'EOF'
more rsl1.csv
m2cross f=2008* a=date,quantity i=rsl1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="並びを逆順する例"
comment=<<'EOF'
横に展開する項目名の並びを逆順にする。
EOF
scp=<<'EOF'
m2cross k=item f=quantity s=date%r i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="データがない場合に項目を追加する例"
comment=<<'EOF'
横に展開する際に、データがない場合に項目を追加する"
EOF
scp=<<'EOF'
more dat2.csv
m2cross k=item f=quantity s=week i=dat2.csv fixfld=Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
