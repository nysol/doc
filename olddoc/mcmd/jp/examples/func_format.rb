#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,0.00726
2,123.456789
3,
4,-0.335
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,amount
1,1000
2,250
3,
4,960
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
\verb|val|を実数として小数点以下2桁に変換する。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='format(${val},"%8.3f")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="指数表現"
comment=<<'EOF'
\verb|val|を指数表現で出力。
EOF
scp=<<'EOF'
mcal c='format(${val},"%e")' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例2
title="文字列との組み合せ"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mcal c='format(${amount},"total amount is %g yen.")' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment,"dat2.csv","rsl3.csv")
