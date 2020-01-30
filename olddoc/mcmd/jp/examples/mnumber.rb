#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Val,Sum
A,29,300
B,35,250
C,15,200
D,23,150
E,10,100
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
Date
20090101
20090101
20090102
20090103
20090103
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Val,Sum
A,3,300
B,1,250
C,2,250
D,1,150
E,1,100
EOF
)}

File.open("dat4.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Val,Sum
A,1,100
B,1,150
C,1,250
D,2,250
E,3,300
EOF
)}

############## 例1
title="数字の連番"
comment=<<'EOF'
Customer項目名順（昇順）に連番を振り「No」という項目名で出力する。
EOF
scp=<<'EOF'
more dat1.csv
mnumber s=Customer a=No i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="Date項目順の連番"
comment=<<'EOF'
Date項目順（昇順）に連番をふる。その際、同じDateには同じNoを振り「No」という項目名で出力する。
EOF
scp=<<'EOF'
more dat2.csv
mnumber k=Date a=No -B i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="Sum項目順の連番(同Rankは同じアルファベットをふる)"
comment=<<'EOF'
Sum項目の多い順（降順）にアルファベットのAから順に連文字を振り「Rank」という項目名で出力する。
また、同Rankの場合は同じアルファベット文字を振ることにする。
EOF
scp=<<'EOF'
more dat3.csv
mnumber a=Rank e=same s=Sum%nr S=A  i=dat3.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="Sum項目順の連番(同Rankは並び順でNoをふる)"
comment=<<'EOF'
Sum項目の多い順（降順）に連番を振り「Rank」という項目名で出力する。
その際、同Rankの場合は並び順でNoを振ることにする。
EOF
scp=<<'EOF'
mnumber a=Rank e=seq s=Sum%nr i=dat3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="Sum項目順の連番(同Rankは同じNoをふる)"
comment=<<'EOF'
Sum項目の多い順（降順）に連番を振り「Rank」という項目名で出力する。
その際、同Rankの場合は同じNoを振ることにする。
EOF
scp=<<'EOF'
mnumber a=Rank e=same s=Sum%nr i=dat3.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## 例6
title="Sum項目順の連番(同Rankの場合は同じRankNoを振り、次のNoはスキップ)"
comment=<<'EOF'
Sum項目の多い順（降順）に連番を振り「Rank」という項目名で出力する。
その際、同Rankの場合は同じRankNoを振り、次のNoはスキップするようにNoを振ることにする。
EOF
scp=<<'EOF'
mnumber a=Rank e=skip s=Sum%nr i=dat3.csv o=rsl6.csv
more rsl6.csv
EOF
run(scp,title,comment)

############## 例7
title="10から始まる連番"
comment=<<'EOF'
Sum項目の小さい順（昇順）に10から始まる連番を振り「Score」という項目名で出力する。
その際、同Rankの場合は同じRankNoを振り、次のNoはスキップするようにNoを振ることにする。
EOF
scp=<<'EOF'
more dat4.csv
mnumber a=Score e=same s=Sum%n S=10 i=dat4.csv o=rsl7.csv
more rsl7.csv
EOF
run(scp,title,comment)

############## 例8
title="10から始まる5つ飛びの連番"
comment=<<'EOF'
Sum項目の小さい順番（昇順）に10から始まる5つ飛びの連番を振り「Score」という項目名で出力する。
また、同Rankの場合は同じNoを振ることにする。
EOF
scp=<<'EOF'
mnumber a=Score e=same s=Sum%n S=10 I=5 i=dat4.csv o=rsl8.csv
more rsl8.csv
EOF
run(scp,title,comment)
