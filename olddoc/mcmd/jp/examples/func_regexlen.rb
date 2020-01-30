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

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,漢漢あbbbいyy
2,漢あbいいy
3,
4,bあいあbbいあ
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
正規表現\verb|c.*a|に最も長くマッチする部分文字列の長さを得る。
マッチした部分文字列については\verb|regexstr|と同じ入力データを使っているので、比較すると分かりやすい。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexlen($s{str},"c.*a")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="マルチバイト文字"
comment=<<'EOF'
正規表現\verb|"あ.*い"|に最も長くマッチする部分文字列の長さを得る。
ただし、以下ではマルチバイト文字対応でないregexlen関数を使っているので、
文字数ではなくバイト数を返している。
EOF
scp=<<'EOF'
more dat2.csv
mcal c='regexlen($s{str},"あ.*い")' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="マルチバイト文字2"
comment=<<'EOF'
正規表現\verb|"あ.*い"|に最も長くマッチする部分文字列の長さを得る。
regexlenw関数を使うと、正しくマルチバイト文字を扱ってくれる。
EOF
scp=<<'EOF'
mcal c='regexlenw($s{str},"あ.*い")' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

