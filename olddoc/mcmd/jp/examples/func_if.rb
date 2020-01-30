#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,time
1,101215
2,210110
3,
4,120001
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,1
2,0
3,
4,-2
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,10
2,0
3,-5
4,0
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
time項目が数値として120000以下であれば"AM"、そうでなければ"PM"を出力する。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='if(${time}<=120000,"AM","PM")' a=ampm i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="異なる型を指定した場合"
comment=<<'EOF'
第2パラメータと第3パラメータに異なる型を指定するとエラーとなる。
EOF
scp=<<'EOF'
mcal c='if(${time}<=120000,"am",1)' a=ampm i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)


############## 例3
title="真偽値による条件選択"
comment=<<'EOF'
\verb|$b{項目名}|によって、データ上の値"1"は真、
"0"は偽、そしてその他の値はNULLとして解釈される。
EOF
scp=<<'EOF'
more dat2.csv
mcal c='if($b{val},"true","false")' a=bool i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="時刻型として比較"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='if($t{time}<=0t120000,"am","pm")' a=ampm i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="if関数のネスト"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat3.csv
mcal c='if(${val}>0,"plus",if(${val}<0,"minus","zero"))' a=sign i=dat3.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

