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
C,20081003,60
C,20081219,20
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
指定した項目の値(顧客)が同じであれば同一のファイルに出力にされるように2つのファイルに分割する
EOF
scp=<<'EOF'
more dat2.csv
mshuffle f=顧客 d=./dat/d n=2 i=dat2.csv
ls ./dat
more ./dat/d_0
more ./dat/d_1
EOF
system("rm -rf dat")
run(scp,title,comment)


############## 例2
title="f=を指定しない例"
comment=<<'EOF'
f=を指定せず2つのファイルに分割する。
行番号のhash値を用いるので、2つのファイルの行数はほぼ等しくなる。
EOF
scp=<<'EOF'
more dat2.csv
mshuffle d=./dat/d n=2 i=dat2.csv
ls ./dat
more ./dat/d_0
more ./dat/d_1
EOF
system("rm -rf dat")
run(scp,title,comment)

############## 例3
title="v=,f=の指定"
comment=<<'EOF'
v=2,1を指定することで、ファイル0(d\_0)には2つのhash値を割り当て、
ファイル1(d\_1)には1つのhash値を割り当てて分割する。
EOF
scp=<<'EOF'
more dat2.csv
mshuffle f=顧客 d=./dat/d v=2,1 i=dat2.csv
ls ./dat
more ./dat/d_0
more ./dat/d_1
EOF
system("rm -rf dat")
run(scp,title,comment)

############## 例4
title="v=の指定"
comment=<<'EOF'
例3をf=の指定なしで実行する。
行番号のhash値を用いるので、この場合は出力行数の比と重みの比がほぼ等しくなる。
EOF
scp=<<'EOF'
more dat2.csv
mshuffle d=./dat/d v=2,1 i=dat2.csv
ls ./dat
more ./dat/d_0
more ./dat/d_1
EOF
system("rm -rf dat")
run(scp,title,comment)


