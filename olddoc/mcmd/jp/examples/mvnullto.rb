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
title="nullを文字列`null'に置換する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mvnullto vf=items v=null i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="分かりやすく区切り文字を.(ドット)にした例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mvnullto vf=items v=null delim=. i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="nullを直前の値に置換する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mvnullto vf=items -p i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="O=を指定することで、null以外は全て指定の値に置換される"
comment=<<'EOF'
EOF
scp=<<'EOF'
mvnullto vf=items v=null O=X i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)


