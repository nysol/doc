#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

# ../../../scp/mkTex.rb ではなく、./mkTex.rb を使っている。
# 実行例で、漢字交じりで1行が長いログを掲載するのに
# 従来の mkTex.rb では改行がうまく処理できないので、
# zenhan() と lenw() 関数を使って長いログのお尻を切り捨てる
# (折り返しではない)ように変更してある。

File.open("text/test.txt","w"){|fpw| fpw.write(
<<'EOF'
子どもはリンゴがすきです。
望遠鏡で泳ぐ少女を見た。
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|text|ディレクトリに文書ファイル\verb|test.txt|を置き、
形態素解析を実行する。結果は\verb|csv|ディレクトリに出力する。
EOF
scp=<<'EOF'
more text/test.txt
mjuman.rb I=text O=csv
more csv/test.txt
EOF
run(scp,title,comment)

############## 例1
title="JUMANの結果（オリジナル）も出力する例"
comment=<<'EOF'
JUMANの結果（オリジナル）も\verb|juman|ディレクトリに出力しておく。
EOF
scp=<<'EOF'
more text/test.txt
mjuman.rb I=text O=csv P=juman
more juman/test.txt
EOF
run(scp,title,comment)

