#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str1,str2,str3
1,abc,def,ghi
2,A,,CDE
3,,,
4,,,XY
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
3つの項目str1,str2,str3を\verb|"#"|の区切り文字を挿入して併合する。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='cat("#",$s{str1},$s{str2},$s{str3})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例1
title="tokenが空文字の場合"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='cat("",$s{str1},$s{str2},$s{str3})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)


############## 例2
title="ワイルドカードを利用した例"
comment=<<'EOF'
\verb|str|から始まる項目(\verb|str1,str2,str3|)をワイルドカード「\verb|str*|」によって指定している。
EOF
scp=<<'EOF'
mcal c='cat("",$s{str*})' a=rsl i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

