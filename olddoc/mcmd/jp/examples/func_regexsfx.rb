#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,xcbbbayy
2,xxcbaay
3,
4,bacabbca
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
正規表現\verb|c.*a|に最も長くマッチする部分文字列のサフィックスを得る。
例えば\verb|id=4|では、$str$項目の\verb|cabbca|にマッチしており、そのサフィックス
すなわちnull文字を返している。
\verb|regexstr,regexpfx|と同じ入力データを使っているので、比較すると分かりやすい。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexsfx($s{str},"c.*a")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

