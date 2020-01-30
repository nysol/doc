#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,time
1,20000101121103
2,20121021111209.123
3,211209
4,211209.123
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='second($t{time})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="文字列とし出力"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='seconds($t{time})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="マイクロ秒を出力"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='usecond($t{time})' a=rsl i=dat1.csv o=rsl3.csv
more rsl3.csv
mcal c='useconds($t{time})' a=rsl i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

