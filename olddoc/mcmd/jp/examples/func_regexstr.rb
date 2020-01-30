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
正規表現\verb|c.*a|に最も長くマッチする部分文字列を得る。
\verb|id=2|では、\verb|cba|もしくは\verb|cbaa|いずれの部分文字列にもマッチしたと考えることができるが、
本関数では、より長くマッチした文字列を返す。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexstr($s{str},"c.*a")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

