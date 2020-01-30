#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,caabaa
2,acabaaa
3,
4,cbcbcc
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|id=1,id=2|共に、正規表現で示された\verb|c|に続く\verb|aa|を含んでいるので真を返す。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexs($s{str},"c.*aa")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例1
title="先頭一致"
comment=<<'EOF'
正規表現\verb|.*c|を$str$項目が含むのは\verb|id=3|以外全ての行である。
EOF
scp=<<'EOF'
mcal c='regexs($s{str},".*c")' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)


