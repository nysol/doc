#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("in1","w"){|fpw| fpw.write(
<<'EOF'
fld1,fld2,fld3
p,q,3
x,y,1
x,y,5
EOF
)}

File.open("in2","w"){|fpw| fpw.write(
<<'EOF'
fld1,fld2,fld3
a,c,2
a,c,4
EOF
)}


File.open("in3","w"){|fpw| fpw.write(
<<'EOF'
fld1,fld2,fld3
p,q,2
x,y,4
x,y,5
EOF
)}

File.open("in4","w"){|fpw| fpw.write(
<<'EOF'
fld1,fld2,fld3
a,c,1
a,c,3
p,q,3
x,y,5
x,y,6
EOF
)}

############## 例1
title="文字列昇順ソートでファイル併合する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more in1
more in2
mmerge k=fld1,fld2 i=in1,in2 o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="数字列昇順ソートでファイル併合する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more in3
more in4
mmerge k=fld3%n,fld1 i=in3,in4 o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
