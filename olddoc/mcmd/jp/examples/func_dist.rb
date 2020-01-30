#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,x1,y1,x2,y2
1,0,0,1,1
2,0,1,2,0
3,,,,
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,x1,y1,x2,y2
1,a,b,a,c
2,0,1,0,1
3,,,,
EOF
)}


############## 例1
title="ユークリッド距離"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='dist("euclid",${x1},${y1},${x2},${y2})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="都市ブロック距離"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='dist("cityblock",${x1},${y1},${x2},${y2})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="ハミング距離"
comment=<<'EOF'
ハミング距離の計算では、値を文字列として指定していることに注意する。
EOF
scp=<<'EOF'
more dat2.csv
mcal c='dist("hamming",$s{x1},$s{y1},$s{x2},$s{y2})' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

