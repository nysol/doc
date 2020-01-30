#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
items
b a c
c c
e a a
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,taxo
a,X Y
b,X
c,Z Z
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
items1,items2
b a c,b b
c c,a d
e a a,a a
EOF
)}

File.open("ref2.csv","w"){|fpw| fpw.write(
<<'EOF'
item,taxo
a,X
b,X
c,Y
d,Y
EOF
)}

############## 例1
title="ベクトルで置換する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mvreplace vf=items K=item m=ref1.csv f=taxo i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="複数項目に対して適用する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
more ref2.csv
mvreplace vf=items1,items2 K=item m=ref2.csv f=taxo i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
