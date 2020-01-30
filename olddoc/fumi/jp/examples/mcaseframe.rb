#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

# ../../../scp/mkTex.rb ではなく、./mkTex.rb を使っている。
# 実行例で、漢字交じりで1行が長いログを掲載するのに
# 従来の mkTex.rb では改行がうまく処理できないので、
# zenhan() と lenw() 関数を使って長いログのお尻を切り捨てる
# (折り返しではない)ように変更してある。

############## 例1
title="基本例"
comment=<<'EOF'
前節の解説で用いてる例。1行が1つの格フレームとなっている。
EOF
scp=<<'EOF'
more xml/test.txt
mcaseframe.rb I=xml o=caseframe.csv
more caseframe.csv
EOF
run(scp,title,comment)

############## 例1
title="key型フォーマットによる出力"
comment=<<'EOF'
\verb|-key|オプションを付加して実行すると、
用言と、その用言に係る格助詞句が行に展開されて出力される。
EOF
scp=<<'EOF'
mcaseframe.rb -key I=xml o=caseframe2.csv
more caseframe2.csv
EOF
run(scp,title,comment)

