#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
vec
b:a:c
x:p
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,vec1,vec2
1,a,b
2,p,q
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
コロンを区切り文字として、ベクトル項目\verb|vec|の要素を並べ替える。
EOF
scp=<<'EOF'
more dat1.csv
mvsort vf=vec delim=: i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="delimを指定しないと"
comment=<<'EOF'
delimを指定していないので\verb|b:a:c|や\verb|x:p|は一つの要素として解釈される。
EOF
scp=<<'EOF'
mvsort vf=vec i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="カンマを区切り文字にする"
comment=<<'EOF'
区切り文字をカンマにした場合は、ベクトル全体がダブルクオーテーションで囲われることで
CSVの区切り文字との区別がつけられる。
EOF
scp=<<'EOF'
more dat2.csv
mvcat vf=vec1,vec2 a=vec3 delim=, i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

