#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
date,customer
20081201,A
20081202,A
20081202,B
20081202,B
20081203,C
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|date|項目を単位に重複行を削除し単一にする。
EOF
scp=<<'EOF'
more dat1.csv
muniq k=date i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="複数の項目での重複行の削除"
comment=<<'EOF'
\verb|date|と\verb|customer|項目を単位に重複行を削除し単一にする。
EOF
scp=<<'EOF'
muniq k=date,customer i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
