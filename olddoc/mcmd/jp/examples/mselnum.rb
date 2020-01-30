#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,5.1
2,5
3,-2.0
4,
5,2.0
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|val|項目が2以上5以下の行、すなわち\verb|id=2,5|の行を選択する。
EOF
scp=<<'EOF'
more dat1.csv
mselnum f=val c='[2,5]' i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="片側範囲"
comment=<<'EOF'
\verb|val|項目が2以上の行、すなわち\verb|id=1,2,5|の行を選択する。
EOF
scp=<<'EOF'
mselnum f=val c='[2,]' i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

