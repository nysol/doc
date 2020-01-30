#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
key1,key2,v1,v2
A,X,1,a
A,Y,2,b
A,Y,3,c
B,X,4,d
B,Y,5,e
EOF
)}

############## 例1
title="配列として出力する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcsv2json f=v1,v2 i=dat1.csv
EOF
run(scp,title,comment)

############## 例2
title="オブジェクト(key-value)として出力する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcsv2json h=v1,v2 i=dat1.csv
EOF
run(scp,title,comment)

############## 例3
title="項目指定によってオブジェクトとして出力する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcsv2json p=v2:v1 i=dat1.csv
EOF
run(scp,title,comment)

############## 例4
title="キー項目を指定する例"
comment=<<'EOF'
\verb|key1|項目が\verb|A|の3行が一つの配列として出力され、
続いて\verb|key1=B|の2行が一つの配列として出力される。
EOF
scp=<<'EOF'
mcsv2json k=key1 f=v1 i=dat1.csv
EOF
run(scp,title,comment)

############## 例5
title="キー項目のネスト例"
comment=<<'EOF'
\verb|key1=A|かつ\verb|key2=X|の1行が一つの配列として出力され、
\verb|key1=A|かつ\verb|key2=Y|の2行が一つの配列として出力され、
それら2つの配列(すなわち\verb|key1=A|の行)がさらに一つの配列として括られる。
EOF
scp=<<'EOF'
mcsv2json k=key1,key2 f=v1 i=dat1.csv
EOF
run(scp,title,comment)

############## 例1
title="行を配列で括らずにフラットに出力する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcsv2json f=v1,v2 -flat i=dat1.csv
EOF
run(scp,title,comment)


