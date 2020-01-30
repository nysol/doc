#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,time
1,000103
2,235959
3,235959.123
4,000000
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,time
1,20130901000103
2,20130902000103
3,20130902000103.123
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='tseconds($t{time})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="日付が異なっても結果は同じ"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mcal c='tseconds($t{time})' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例2
title="マイクロ秒"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='tuseconds($t{time})' a=rsl i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)


