#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
date,val
20130406,1
20130407,2
20130408,3
20130409,4
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
store,date,val
a,20130406,1
a,20130407,2
a,20130408,3
a,20130409,4
b,20130406,11
b,20130407,12
b,20130408,13
b,20130409,14
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mwindow wk=date:win t=2 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="基準行を先頭にした例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mwindow wk=date:win t=3 -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="指定行数に満たない窓も出力する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mwindow wk=date:win t=3 -r -n i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="キー項目を指定した例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mwindow k=store wk=date:win t=2 i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="前日までの移動平均を求める"
comment=<<'EOF'
冒頭に示した移動平均の例では、窓における最終日を基準として平均を計算している。
時に、基準日を前日として移動平均を計算したいケースがある。
そういった場合は\verb|mslide|で1日日付をずらしてから本コマンドを使えばよい。
その例を以下に示す。
EOF
scp=<<'EOF'
mslide f=date:date2 s=date i=dat1.csv o=rsl5.csv
more rsl5.csv
mwindow wk=date2:win t=2 i=rsl5.csv o=rsl6.csv
more rsl6.csv
EOF
run(scp,title,comment)

