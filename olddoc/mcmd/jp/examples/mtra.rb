#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,item
A,a
A,b
B,c
B,d
B,e
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|customer|を単位に\verb|item|をスペース区切りで結合し、
\verb|transaction|という項目名で出力する。
EOF
scp=<<'EOF'
more dat1.csv
mtra k=customer f=item:transaction i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="アイテムの区切り文字を-(ハイフン）で実行"
comment=<<'EOF'
EOF
scp=<<'EOF'
mtra k=customer f=item:transaction delim=- i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="アイテムを降順に並べ替えてから変換"
comment=<<'EOF'
EOF
scp=<<'EOF'
mtra k=customer s=item%r f=item:transaction i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

