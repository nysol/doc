#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,itemID,10月
a,xx,11
b,yy,122
c,zz,
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
a,xx,11
b,yy,122
c,zz,
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
項目名の「顧客」を「cust」に、「10月」を「Oct.」に変更する。
EOF
scp=<<'EOF'
more dat1.csv
mfldname f=顧客:cust,10月:Oct. i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="項目名変更"
comment=<<'EOF'
項目名を\verb|x,y,z|に変更する。
EOF
scp=<<'EOF'
mfldname n=x,y,z i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="項目名行がないデータ"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mfldname -nfni n=x,y,z i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
