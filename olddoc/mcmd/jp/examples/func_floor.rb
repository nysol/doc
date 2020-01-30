#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,3.28
2,3.82
3,
4,-0.6
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,1341.28
2,188
3,1.235E+3
4,-1.235E+3
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
小数点以下一桁目を切り捨てる。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='floor(${val})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="基本例"
comment=<<'EOF'
小数点以下二桁目を切り捨てる。
EOF
scp=<<'EOF'
mcal c='floor(${val},0.1)' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="基数0.5の例"
comment=<<'EOF'
0.5を基数として切り捨てる。
EOF
scp=<<'EOF'
mcal c='floor(${val},0.5)' a=rsl i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="基数10の例"
comment=<<'EOF'
一桁目を切り捨てる。
EOF
scp=<<'EOF'
more dat2.csv
mcal c='floor(${val},10)' a=rsl i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

