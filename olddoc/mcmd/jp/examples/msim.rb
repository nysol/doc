#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
x,y,z
14,0.17,-14
11,0.2,-1
32,0.15,-2
13,0.33,-2
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
key,x,y,z
A,14,0.17,-14
A,11,0.2,-1
A,32,0.15,-2
B,13,0.33,-2
B,10,0.8,-5
B,15,0.45,-9
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
x,y,z
1,1,0
1,0,1
1,0,1
0,1,1
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|x、y、z|項目の2項目間の組み合わせについて
ピアソンの積率相関係数とコサインを計算する。
EOF
scp=<<'EOF'
more dat1.csv
msim c=pearson,cosine f=x,y,z i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="対角行列、上三角行列を出力"
comment=<<'EOF'
\verb|x、y、z|項目の2項目間の組み合わせについて
ピアソンの積率相関係数とコサインを計算する。(dオプションあり)
EOF
scp=<<'EOF'
msim c=pearson,cosine f=x,y,z -d i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
############## 例3
title="キー単位での計算"
comment=<<'EOF'
\verb|key|項目を単位にして計算する。
EOF
scp=<<'EOF'
more dat2.csv
msim k=key c=pearson,cosine f=x,y,z i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="類似度名の指定"
comment=<<'EOF'
01値のデータに付いての計算。ハミング距離とphi係数を計算する。
EOF
scp=<<'EOF'
more dat3.csv
msim c=hamming,phi f=x,y,z i=dat3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="類似度名の変更"
comment=<<'EOF'
01値のデータに付いての計算。ハミング距離とphi係数を計算し、
出力項目名を変更する。
EOF
scp=<<'EOF'
msim c=hamming:ハミング距離,phi:ファイ係数 a=変数1,変数2 f=x,y,z i=dat3.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)
