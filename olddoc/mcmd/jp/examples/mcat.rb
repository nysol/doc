#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,日付,金額
A,20081201,10
B,20081002,40
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,日付,金額
A,20081207,20
A,20081213,30
B,20081209,50
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,日付,数量
A,20081201,3
B,20081002,1
EOF
)}

############## 例1
title="同一項目名ファイルの併合"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
more dat2.csv
mcat i=dat1.csv,dat2.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="項目名の異なるファイルの併合"
comment=<<'EOF'
\verb|i=|の最初のファイル\verb|dat1.csv|の項目「顧客,日付,金額」の3項目を併合する。
しかし、\verb|dat3.csv|には「金額」項目がないので、エラーとなる。
ただし、\verb|dat1.csv|の内容は既に出力されていることに注意する。
EOF
scp=<<'EOF'
more dat3.csv
mcat i=dat1.csv,dat3.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="項目名の異なるファイルの併合2"
comment=<<'EOF'
前例に\verb|-nostop|オプションを付けると、項目が見つからないデータについてはNULL値を出力するようになり、
途中でエラー終了することはなくなる。
その他にも、項目が見つからなかった場合の動作を変更するオプションとして、\verb|skip,force|がある。
詳しくはパラメータの説明を参照されたい。
EOF
scp=<<'EOF'
more dat3.csv
mcat -nostop i=dat1.csv,dat3.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="項目名を指定して併合"
comment=<<'EOF'
\verb|f=|で項目名を指定すると、それら指定した項目のみを併合する。
EOF
scp=<<'EOF'
mcat f=顧客,日付 i=dat2.csv,dat3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="標準入力の併合"
comment=<<'EOF'
\verb|-stdin|を指定することで、\verb|dat2.csv|を標準入力から追加する。
EOF
scp=<<'EOF'
mcat -stdin i=dat1.csv o=rsl5.csv <dat2.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## 例6
title="ファイル名項目を追加"
comment=<<'EOF'
\verb|-add_fname|を指定すると、元ファイルの名前を\verb|fileName|項目で追加する。
標準入力のファイル名は\verb|/dev/stdin|となる。
EOF
scp=<<'EOF'
mcat -add_fname -stdin i=dat1.csv o=rsl6.csv <dat2.csv
more rsl6.csv
EOF
run(scp,title,comment)

############## 例7
title="ワイルドカード指定"
comment=<<'EOF'
カレントディレクトリに\verb|dat1.csv,dat2.csv,dat3.csv|の3つのCSVファイルがあったとして、
それらを全て併合するのにワイルドカード\verb|dat*.csv|を指定する。
EOF
scp=<<'EOF'
more dat1.csv
more dat2.csv
more dat3.csv
mcat -force i=dat*.csv o=rsl7.csv
more rsl7.csv
EOF
run(scp,title,comment)

############## 例8
title="同一ファイルの複数回併合"
comment=<<'EOF'
同一ファイルを複数指定することも可能である。
EOF
scp=<<'EOF'
mcat i=dat1.csv,dat1.csv,dat1.csv o=rsl8.csv
more rsl8.csv
EOF
run(scp,title,comment)

