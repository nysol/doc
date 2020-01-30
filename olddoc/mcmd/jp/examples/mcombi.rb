#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,item
A,a1
A,a2
A,a3
B,a4
B,a5
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|customer|項目を単位に、\verb|item|項目の2アイテムの組み合わせを求め、
\verb|item1,item2|という項目名で出力する。
\verb|k=,f=|で指定していない項目(ここでは\verb|item|項目)は、キーの最終行の値が出力される。
EOF
scp=<<'EOF'
more dat1.csv
mcombi k=customer f=item n=2 a=item1,item2 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="基本例2"
comment=<<'EOF'
\verb|-dup|オプションを指定すると同一のアイテムの組み合せも出力される。
EOF
scp=<<'EOF'
mcombi k=customer f=item n=2 a=item1,item2 i=dat1.csv o=rsl2.csv -dup
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="順列を求める例"
comment=<<'EOF'
\verb|customer|項目を単位に、\verb|item|項目の2アイテムの順列を求め、
\verb|item1,item2|という項目名で出力する。
EOF
scp=<<'EOF'
mcombi k=customer f=item n=2 a=item1,item2 -p i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="順列を求める例"
comment=<<'EOF'
\verb|item|項目を降順に並べ替えた後、
\verb|item|項目の2アイテムの順列を求める。
EOF
scp=<<'EOF'
mcombi k=customer f=item n=2 s=item%r a=item1,item2 -p i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
