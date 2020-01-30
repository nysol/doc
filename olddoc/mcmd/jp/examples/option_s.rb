#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
A,1
B,1
B,2
A,2
B,3
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
\verb|id|項目で並べ替えた後、\verb|val|項目の累計を計算する。
EOF
scp=<<'EOF'
more dat1.csv
maccum s=id k=id f=val:val_accum i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)


############## 例1
title="並べ替え方法を指定する"
comment=<<'EOF'
\verb|val|項目を数値降順で並べ替えた後、\verb|val|項目の累計を計算する。
EOF
scp=<<'EOF'
more dat1.csv
maccum s=id,val%nr k=id f=val:val_accum i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)


