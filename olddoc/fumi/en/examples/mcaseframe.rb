#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

# ../../../scp/mkTex.rb ではなく、./mkTex.rb を使っている。
# 実行例で、漢字交じりで1行が長いログを掲載するのに
# 従来の mkTex.rb では改行がうまく処理できないので、
# zenhan() と lenw() 関数を使って長いログのお尻を切り捨てる
# (折り返しではない)ように変更してある。

############## 例1
title="Basic Example"
comment=<<'EOF'
Example used in the previous section. One line has become one case frame.
EOF
scp=<<'EOF'
more xml/test.txt
mcaseframe.rb I=xml o=caseframe.csv
more caseframe.csv
EOF
run(scp,title,comment)

############## Example 2
title="Output of key type format"
comment=<<'EOF'
When executing by adding the option \verb|-key|, 
case particle influencing inflectable word from the line is saved in output. 
EOF
scp=<<'EOF'
mcaseframe.rb -key I=xml o=caseframe2.csv
more caseframe2.csv
EOF
run(scp,title,comment)

