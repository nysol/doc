#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量
A,1
B,2
C,1
D,3
E,1
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,性別
A,女性
B,男性
E,女性
EOF
)}

File.open("ref2.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客ID,性別
A,女性
B,男性
E,女性
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量
A,1
A,2
A,3
B,1
D,1
D,2
EOF
)}

File.open("ref3.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客
A
A
D
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
入力ファイルにある「顧客」項目と、参照ファイルにある「顧客」項目が同じ値を持つ入力ファイルの行を選択する。
それ以外のデータは\verb|oth.csv|に出力する。
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mcommon k=顧客 m=ref1.csv u=oth.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
more oth.csv
EOF
run(scp,title,comment)

############## 例2
title="同じ値を持たない入力ファイルの行選択"
comment=<<'EOF'
\verb|-r|オプションを付けることで、条件が逆転し、参照ファイルにない「顧客」を選択することになる。
EOF
scp=<<'EOF'
mcommon k=顧客 m=ref1.csv -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="結合キー項目名が異なる場合"
comment=<<'EOF'
結合キーの項目名が異なる場合は、\verb|K=|で指定する。
EOF
scp=<<'EOF'
more ref2.csv
mcommon k=顧客 K=顧客ID i=dat1.csv m=ref2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="キー項目に重複行がある場合の例"
comment=<<'EOF'
参照ファイルと入力ファイルのキー項目に重複行があっても選択可能。
EOF
scp=<<'EOF'
more dat3.csv
more ref3.csv
mcommon k=顧客 m=ref3.csv -r i=dat3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
