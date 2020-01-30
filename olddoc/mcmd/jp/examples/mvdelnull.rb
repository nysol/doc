#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
items
b a  c
 c c
e a   b 
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
items
b.a..c
.c.c
e.a...b.
EOF
)}


############## 例1
title="nullを削除する基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mvdelnull vf=items i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="分かりやすく区切り文字を.(ドット)にした例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mvdelnull vf=items delim=. i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="項目名を変更して出力"
comment=<<'EOF'
EOF
scp=<<'EOF'
mvdelnull vf=items:new i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="-Aを指定することで追加項目として出力"
comment=<<'EOF'
EOF
scp=<<'EOF'
mvdelnull vf=items:new -A i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
