#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,abc
2,3.1415
3,
4,hello world!
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,こんにちは
2,大阪
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='length($s{str})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例1
title="マルチバイト文字を含む例"
comment=<<'EOF'
以下はutf-8でエンコーディングされた日本語を用いた例である。
utf-8の日本語は1文字3バイトでエンコーディングされているので、
length関数では日本語としての文字数ではなく、そのバイト数を返す。
EOF
scp=<<'EOF'
more dat2.csv
mcal c='length($s{str})' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例1
title="ワイド文字として扱う例"
comment=<<'EOF'
lengthwを使うと、内部で文字列をワイド文字に変換するので、マルチバイト文字1文字を正しく認識して計算する。
EOF
scp=<<'EOF'
mcal c='lengthw($s{str})' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

