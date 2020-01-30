#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
fld
date:20120304 time:121212
date:20101204 time:011309.1234
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
fld,fld2
2010/11/20,2010/11/21
2010/1/1,2010/1/2
2011/01/01,2010/01/02
2010/1/01,2010/1/02
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
fld
2010 11 20 12:34:56
2011 01 01 23:34:56
2010  1 01 123455
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|fld|項目から日付・時刻を抽出し変換する。
\verb|fld|項目には「date:年月日 time:時分秒.マイクロ秒」の形式で日付・時刻が格納されているので、
\verb|c=|パラメータには「\verb|date:%Y%m%d time:%H%M%s|」と指定している。
EOF
scp=<<'EOF'
more dat1.csv
mdformat f=fld c='date:%Y%m%d time:%H%M%s' i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="項目の追加"
comment=<<'EOF'
\verb|fld1|項目、\verb|fld2|項目には「年/月/日」形式で日付が格納されているので、
\verb|c=|パラメータには「\verb|%Y/%m/%d|」と指定している。
\verb|-A|オプションを使用し、変換結果を新たな\verb|f1|、\verb|f2|項目に抽出する。
EOF
scp=<<'EOF'
more dat2.csv
mdformat f=fld:f1,fld2:f2 c=%Y/%m/%d i=dat2.csv -A o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="抽出がうまくいかない例"
comment=<<'EOF'
\verb|fld|項目には「年 月 日 時:分:秒」形式で日付が格納されているので、
\verb|c=|パラメータには「\verb|%Y %m %d %H:%M:%S|」と指定している。
しかし形式が異なる行は抽出に失敗している。
EOF
scp=<<'EOF'
more dat3.csv
mdformat f=fld:f1 c='%Y %m %d %H:%M:%S' i=dat3.csv -A o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)


