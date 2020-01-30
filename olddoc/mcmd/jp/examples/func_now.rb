#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id
1
2
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='now()' a=rsl i=dat1.csv o=rsl1-1.csv
more rsl1-1.csv
mcal c='unow()' a=rsl i=dat1.csv o=rsl1-2.csv
more rsl1-2.csv
EOF
run(scp,title,comment)

############## 例2
title="時刻のみ切り出し"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='time(now())' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例2
title="日付のみ切り出し"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='date(now())' a=rsl i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

