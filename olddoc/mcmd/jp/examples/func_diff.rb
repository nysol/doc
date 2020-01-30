#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,date
1,19641010
2,20000101
3,20130831
4,20130901
5,20130902
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,time
1,20120101000000
2,20120101011112
3,
4,20111231235000
5,20111231235000.123456
EOF
)}

############## 例1
title="月単位での期間"
comment=<<'EOF'
\verb|date|項目から2013年9月1日までの経過期間を日数で計算する。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='diffday(0d20130901,$d{date})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="分単位での期間"
comment=<<'EOF'
\verb|time|項目から2012年1月1日 00時00分00秒までの経過期間を分単位で計算する。
EOF
scp=<<'EOF'
more dat2.csv
mcal c='diffmonth(0t20120101000000,$t{time})' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="マイクロ秒単位での期間"
comment=<<'EOF'
\verb|time|項目から2012年1月1日 00時00分00秒までの経過期間を秒単位およびマイクロ秒単位で計算する。
EOF
scp=<<'EOF'
mcal c='diffsecond(0t20120101000000,$t{time})' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
mcal c='diffusecond(0t20120101000000,$t{time})' a=rsl i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

