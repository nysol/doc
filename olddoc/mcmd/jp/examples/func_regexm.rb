#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,caabaa
2,acabaaa
3,
4,bbcbcc
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|id=1,id=2|共に、正規表現で示された\verb|c|に続く\verb|aa|を含んでいるが、
\verb|id=2|ではマッチする範囲が部分的(2文字目の\verb|c|から最後まで)であるために偽となっている。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexm($s{str},"c.*aa")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="末尾一致"
comment=<<'EOF'
正規表現\verb|.*c|で$str$項目の全体がカバーされるのは\verb|id=4|の行のみである。
EOF
scp=<<'EOF'
mcal c='regexm($s{str},".*c")' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="空文字マッチ"
comment=<<'EOF'
正規表現\verb|^$|で\verb|id=3|の空文字にマッチする。
EOF
scp=<<'EOF'
mcal c='regexm($s{str},"^$")' a=rsl i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)


