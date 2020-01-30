#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,quantity
A,5
B,10
C,15
D,2
E,50
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|quantity|項目の値が最小以上10未満を\verb|low|、
10以上20未満を\verb|middle|、20以上最大未満を\verb|high|という文字列に置換する。
EOF
scp=<<'EOF'
more dat1.csv
mchgnum f=quantity R=MIN,10,20,MAX v=low,middle,high i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="パラメータ範囲にイコールをつける例"
comment=<<'EOF'
\verb|quantity|項目の値が最小より多く10以下を\verb|low|、
10より多く20以下を\verb|middle|、20より多く最大以下を\verb|high|という文字列に置換する。
EOF
scp=<<'EOF'
mchgnum f=quantity R=MIN,10,20,MAX v=low,middle,high -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
############## 例3
title="数値範囲リストに合致しない値を置換"
comment=<<'EOF'
\verb|quantity|項目の値が10以上20未満を\verb|low|、
20以上30未満を\verb|middle|、30以上最大未満を\verb|high|、
数量が10より小さい値は\verb|out of range|という文字列に置換する。
EOF
scp=<<'EOF'
mchgnum f=quantity R=10,20,30,MAX v=low,middle,high O="out of range" i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
############## 例4
title="新たな項目の追加"
comment=<<'EOF'
\verb|quantity|項目の値が最小以上10未満を\verb|low|、
10以上20未満を\verb|middle|、20以上最大未満を\verb|high|という文字列に置換し
\verb|evaluate|という項目名で出力する。
EOF
scp=<<'EOF'
mchgnum f=quantity:evaluate R=MIN,10,20,MAX v=low,middle,high -A i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
############## 例5
title="範囲外を項目の値として出力"
comment=<<'EOF'
\verb|quantity|項目の値が10以上20未満を\verb|low|、20以上30未満を\verb|middle|、
30以上最大未満を\verb|high|、数量が10より小さい値は置換しないでそのまま出力する。
EOF
scp=<<'EOF'
mchgnum f=quantity R=10,20,30,MAX v=low,middle,high -F i=dat1.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)
