#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
A,1
B,2
B,2
A,1
B,2
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
カレントディレクトの直下の\verb|tmp|ディレクトリを作業ファイル用のディレクトリとする。
EOF
scp=<<'EOF'
msortf f=val tmpPath=./tmp i=dat1.csv o=rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="環境変数による指定"
comment=<<'EOF'
環境変数によって設定すると、それ以降全てのコマンドがその設定値を使う。
EOF
scp=<<'EOF'
export KG_TmpPath=~/tmp
msortf f=val i=dat1.csv o=rsl1.csv
EOF
run(scp,title,comment)

