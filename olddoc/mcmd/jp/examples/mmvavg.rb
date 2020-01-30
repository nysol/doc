#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,value
1,5
2,1
3,3
4,4
5,4
6,6
7,1
8,4
9,7
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,key,value
1,a,5
2,a,1
3,a,3
4,a,4
5,a,4
6,b,6
7,b,1
8,b,4
9,b,7
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
key,value
a,1
a,2
a,3
a,4
a,5
b,6
b,1
b,4
b,7
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
最初の行は期数に満たないため出力されない。
EOF
scp=<<'EOF'
more dat1.csv
mmvavg s=id f=value t=2 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="基本例2"
comment=<<'EOF'
最初の行は期数に満たないため出力されない。
EOF
scp=<<'EOF'
mmvavg s=id f=value t=2 -w i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="基本例3"
comment=<<'EOF'
指数平滑移動平均(\verb|-exp|)の場合は最初の行から出力される。
EOF
scp=<<'EOF'
mmvavg s=id f=value t=2 -exp i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="キーを指定する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mmvavg s=key,id k=key f=value t=2 i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="指定した期に満たなくても出力する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat3.csv
mmvavg -q k=key f=value t=2 skip=0 i=dat3.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)
