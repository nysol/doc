#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id1
1
2
3
4
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
id2
a
b
c
d
EOF
)}

File.open("ref2.csv","w"){|fpw| fpw.write(
<<'EOF'
id2
a
b
EOF
)}

File.open("ref3.csv","w"){|fpw| fpw.write(
<<'EOF'
id2,val
a,R0
b,R1
c,R2
d,R3
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mpaste m=ref1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="行数が異なる例"
comment=<<'EOF'
入力ファイルと参照ファイルで行数が異なる場合は、少いファイルの行数に合わせる。
EOF
scp=<<'EOF'
more ref2.csv
mpaste m=ref2.csv i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="外部結合"
comment=<<'EOF'
\verb|-n|を指定すると、参照ファイルの行数が少なくても、対応しない入力ファイルの行もNULL値を結合して出力する。
EOF
scp=<<'EOF'
mpaste m=ref2.csv -n i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="結合項目を指定"
comment=<<'EOF'
EOF
scp=<<'EOF'
more ref3.csv
mpaste f=val m=ref3.csv i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
