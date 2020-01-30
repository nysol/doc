#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

# ../../../scp/mkTex.rb ではなく、./mkTex.rb を使っている。
# # 実行例で、漢字交じりで1行が長いログを掲載するのに
# # 従来の mkTex.rb では改行がうまく処理できないので、
# # zenhan() と lenw() 関数を使って長いログのお尻を切り捨てる
# # (折り返しではない)ように変更してある。

File.open("dic1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,見出し語,読み,品詞,カテゴリ,ドメイン
1,連結営業利益,れんけつえいぎょうりえき,普通名詞,抽象物,ビジネス
2,米国債,べいこくさい,,抽象物,ビジネス
3,上方修正,じょうほうしゅうせい,サ変名詞,抽象物,ビジネス
4,日本航空,にほんこうくう,組織名,,
5,夏目漱石,なつめそうせき,人名,日本,姓
6,安倍首相 安倍晋太郎 安倍晋太郎首相,あべしゅしょう,人名,日本,姓名
7,２ちゃんねる にちゃんねる,にちゃんねる,,,
EOF
)}

############## Example1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dic1.csv
mjumandic.rb i=dic1.csv O=jumandic
ls jumandic
more jumandic/jumandic.dic
EOF
run(scp,title,comment)

