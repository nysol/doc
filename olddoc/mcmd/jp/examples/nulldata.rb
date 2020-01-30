#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
A,B,C
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
EOF
)}

############## 例1
title="項目名行ありデータ"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
msetstr v="string" a=X i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="項目名行なしデータ"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
msetstr v="string" -nfn i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

