#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客
A
B
C
D
E
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客
A
A
A
B
B
C
D
D
D
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
0.0から1.0の範囲の実数乱数を生成する。
EOF
scp=<<'EOF'
more dat1.csv
mrand a=rand i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="基本例2"
comment=<<'EOF'
-intで整数乱数
EOF
scp=<<'EOF'
mrand a=rand -int i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="最小値、最大値を決めた乱数の生成"
comment=<<'EOF'
最小値が10、最大値が100の整数の乱数を生成し、\verb|rand|という項目名で出力する。
EOF
scp=<<'EOF'
mrand a=rand -int min=10 max=100 S=1 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
############## 例4
title="キー単位の乱数生成"
comment=<<'EOF'
以下の例は、顧客\verb|A,B,C,D|の4人について同じ顧客には同じ乱数値を振る。
EOF
scp=<<'EOF'
more dat2.csv
mrand k=顧客 -int min=0 max=1 a=rand i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
