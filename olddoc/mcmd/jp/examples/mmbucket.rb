#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,x,y
A,2,7
B,6,7
C,5,6
D,7,5
E,6,4
F,1,3
G,3,3
H,4,2
I,7,2
J,2,1
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,x,y
A,2,7
A,6,7
A,5,6
B,7,5
B,6,4
B,1,3
C,3,3
C,4,2
C,7,2
C,2,1
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
\verb|x、y|項目の件数ができるだけ多次元均等になるように2分割する。
その際、各バケットの数値範囲を\verb|rng.csv|という名前のファイルに出力する。
EOF
scp=<<'EOF'
more dat1.csv
mmbucket f=x:xb,y:yb n=2,2 O=rng.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
more rng.csv
EOF
run(scp,title,comment)

############## 例2
title="出力形式"
comment=<<'EOF'
\verb|id|項目を単位に件数ができるだけ多次元均等になるように\verb|x,y|項目を2分割する。
出力形式はバケット番号とバケット範囲の両方を表示する。
EOF
scp=<<'EOF'
more dat2.csv
mmbucket k=id f=x:xb,y:yb n=2,2 F=2 i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
