#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,birthday
A,19690103
B,
C,19500501
D,
E,
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,date
A,19690103
B,
C,19500501
D,
E,
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
id,seq,val
A,1,1
A,3,2
A,2,
B,2,3
B,1,
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
\verb|birthday|項目がNULL値の場合は\verb|"no value"|に置換する。
EOF
scp=<<'EOF'
more dat1.csv
mnullto f=birthday v="no value" i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="NULL値以外の置換"
comment=<<'EOF'
\verb|birthday|項目がNULL値の場合は、\verb|"no value"|
値がある場合は\verb|"value"|置換し\verb|entry|という項目名に変更して出力する。
EOF
scp=<<'EOF'
mnullto f=birthday:entry v="no value" O="value" i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
############## 例3
title="新しい項目を出力"
comment=<<'EOF'
\verb|birthday|項目がNULL値の場合は\verb|"no value"|、値がある場合は\verb|"value"|に置換し\verb|entry|という項目名で出力する。
EOF
scp=<<'EOF'
mnullto f=birthday:entry v="no value" O="value" -A i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="前行の値に置換"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat3.csv
mnullto f=val -p i=dat3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="キー項目を指定した場合の例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mnullto k=id s=seq f=val -p i=dat3.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

