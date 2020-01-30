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
\verb|x,y|項目それぞれで、件数ができるだけ均等になるように2分割する。
その際、各バケットの数値範囲を\verb|rng1.csv|に出力する。
EOF
scp=<<'EOF'
more dat1.csv
mbucket f=x:xb,y:yb n=2 O=rng1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
more rng1.csv
EOF
run(scp,title,comment)

############## 例3
title="範囲均等化分割"
comment=<<'EOF'
\verb|-rng|オプションを指定すると範囲均等化分割となる。
EOF
scp=<<'EOF'
mbucket f=x:xb,y:yb n=2 -rng O=rng2.csv i=dat1.csv o=rsl2.csv
more rsl2.csv
more rng2.csv
EOF
run(scp,title,comment)


############## 例2
title="キー項目を指定した例"
comment=<<'EOF'
id項目を集計キーとして、\verb|x,y|項目それぞれを件数均等化バケット分割する。
\verb|n=2,3|と指定することで、\verb|x|項目の分割数は2に、
\verb|y|項目の分割数は3となる。
出力形式はバケット番号とバケット範囲の両方を表示する(\verb|F=2|)。
EOF
scp=<<'EOF'
more dat2.csv
mbucket k=id f=x:xb,y:yb n=2,3 F=2 i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)


