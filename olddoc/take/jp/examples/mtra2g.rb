#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
tid,item
T1,C
T1,E
T2,D
T2,E
T2,F
T3,A
T3,B
T3,D
T3,F
T4,B
T4,D
T4,F
T5,A
T5,B
T5,D
T5,E
T6,A
T6,B
T6,D
T6,E
T6,F
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
出現件数が2件以上の類似度グラフ。
上述の解説の中で示した例。
EOF
scp=<<'EOF'
more dat1.csv
mtra2g.rb  S=2 tid=tid item=item i=dat1.csv eo=edge1.csv
more edge1.csv
EOF
run(scp,title,comment)

############## 例2
title="resemblanceを追加"
comment=<<'EOF'
例1に加えてresemblanceが0.4以上を類似度条件に加える。
また\verb|no=|を指定することで、節点情報としてアイテム単独の出現頻度を出力する。
EOF
scp=<<'EOF'
mtra2g.rb  S=2 sim=R th=0.4 tid=tid item=item i=dat1.csv eo=edge2.csv no=node2.csv
more node2.csv
more edge2.csv
EOF
run(scp,title,comment)

