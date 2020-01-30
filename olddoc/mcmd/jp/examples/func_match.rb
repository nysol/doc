#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,f1,f2,f3
1,1,1,1
2,1,0,1
3,,,
4,1,,1
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,s1,s2,s3
1,ab,abx,x
2,abc,xaby,xxab
3,,,
4,#ac,x,x
EOF
)}


############## 例1
title="OR完全一致"
comment=<<'EOF'
\verb|f1,f2,f3|項目のいずれかが\verb|1|であれば真を返す。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='match("1",$s{f1},$s{f2},$s{f3})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="AND完全一致"
comment=<<'EOF'
\verb|f1,f2,f3|項目の全てが文字列\verb|"1"|であれば真を返す。
EOF
scp=<<'EOF'
mcal c='matcha("1",$s{f1},$s{f2},$s{f3})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="OR部分一致"
comment=<<'EOF'
\verb|s1,s2,s3|項目のいずれかが、文字列\verb|ab|を含んでいれば真を返す。
EOF
scp=<<'EOF'
more dat2.csv
mcal c='matchs("ab",$s{s1},$s{s2},$s{s3})' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="AND部分一致"
comment=<<'EOF'
文字列\verb|ab|が\verb|s1,s2,s3|項目の全てに、文字列\verb|ab|が含まれて入れば真を返す。
EOF
scp=<<'EOF'
mcal c='matchas("ab",$s{s1},$s{s2},$s{s3})' a=rsl i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="NULL値の検索"
comment=<<'EOF'
\verb|str|項目がNULL値であれば真を返す。
EOF
scp=<<'EOF'
mcal c='match(nulls(),$s{s1},$s{s2},$s{s3})' a=rsl i=dat2.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

