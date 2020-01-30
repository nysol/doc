#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
node1,node2
a,b
a,c
a,e
b,c
b,e
b,g
c,d
c,g
d,e
e,f
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
類似度をresemblance(sim=R)とし、th=0.4で枝を張り直して得られた研磨グラフ。
\verb|log1.csv|を見ると研磨回数は4回で収束していることがわかる(iter,4)。
出力結果は図\ref{fig:resemblance04}に示されるグラフ。

EOF
scp=<<'EOF'
more dat1.csv
mpolishing.rb ei=dat1.csv ef=node1,node2 sim=R th=0.4 eo=result1.csv log=log1.csv
more result1.csv
more log1.csv
EOF
run(scp,title,comment)

############## 例2
title="PMIによる研磨"
comment=<<'EOF'
類似度をnormalized PMI(sim=P)とし、th=0.2で枝を張り直して得られた研磨グラフ。
出力結果は図\ref{fig:pmi02}に示されるグラフ。

EOF
scp=<<'EOF'
mpolishing.rb ei=dat1.csv ef=node1,node2 sim=P th=0.2 eo=result2.csv
more result2.csv
EOF
run(scp,title,comment)


############## 例3
title="intersectionで1回の研磨"
comment=<<'EOF'
前節の解説で用いてる例。類似度をintersection(sim=T)とし、2件以上(th=2)で枝を張り直し
直接の接続を考慮に入れる例。研磨回数は1回のみ(iter=1)。
出力結果は図\ref{fig:polished2}に示されるグラフ。

EOF
scp=<<'EOF'
mpolishing.rb ei=dat1.csv ef=node1,node2 sim=T th=2 iter=1 eo=result3.csv
more result3.csv
EOF
run(scp,title,comment)

############## 例4
title="直接の接続を考慮しない例"
comment=<<'EOF'
\verb|-indirect|を指定することで、類似度の計算で直接の接続は無視される。
出力結果は図\ref{fig:polished1}に示されるグラフであり、枝が全て消えるため、研磨後の枝データは出力されない。
EOF
scp=<<'EOF'
mpolishing.rb ei=dat1.csv ef=node1,node2 sim=T th=2 eo=result4.csv -indirect
more result4.csv
EOF
run(scp,title,comment)


