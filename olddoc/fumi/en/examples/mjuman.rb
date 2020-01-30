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

############## Example1
title="Basic Example"
comment=<<'EOF'
File \verb|test.txt| is contained in \verb|text| directory for morphological analyisis. The results are saved in \verb|csv| directory. 
EOF
scp=<<'EOF'
more text/test.txt
mjuman.rb I=text O=csv
more csv/test.txt
EOF
run(scp,title,comment)

############## Example2
title="Example of results of JUMAN (original)"
comment=<<'EOF'
JUMAN results (original) is saved in \verb|juman| directory.
EOF
scp=<<'EOF'
more text/test.txt
mjuman.rb I=text O=csv P=juman
more juman/test.txt
EOF
run(scp,title,comment)

