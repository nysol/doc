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

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
tid,item,class
T1,C,cls1
T1,E,cls1
T2,D,cls1
T2,E,cls1
T2,F,cls1
T3,A,cls1
T3,B,cls1
T3,D,cls1
T3,F,cls1
T4,B,cls1
T4,D,cls1
T4,F,cls1
T5,A,cls2
T5,B,cls2
T5,D,cls2
T5,E,cls2
T6,A,cls2
T6,B,cls2
T6,D,cls2
T6,E,cls2
T6,F,cls2
EOF
)}

File.open("taxo.csv","w"){|fpw| fpw.write(
<<'EOF'
item,taxonomy
A,X
B,X
C,Y
D,Z
E,Z
F,Z
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
3件以上で出現する頻出アイテム集合を列挙する。
EOF
scp=<<'EOF'
more dat1.csv
mitemset.rb  S=3 tid=tid item=item i=dat1.csv O=result1
more result1/patterns.csv
more result1/tid_pats.csv
EOF
run(scp,title,comment)

############## 例2
title="アイテム集合のサイズに制限を加えた例"
comment=<<'EOF'
出現頻度が3以上で、アイテム集合のサイズ3のパターンを列挙する。
EOF
scp=<<'EOF'
mitemset.rb S=3 l=3 u=3 tid=tid item=item i=dat1.csv O=result2
more result2/patterns.csv
EOF
run(scp,title,comment)

############## 例3
title="飽和集合の列挙例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mitemset.rb S=3 type=C tid=tid item=item i=dat1.csv O=result3
more result3/patterns.csv
EOF
run(scp,title,comment)

############## 例4
title="極大集合の列挙例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mitemset.rb S=3 type=M tid=tid item=item i=dat1.csv O=result4
more result4/patterns.csv
EOF
run(scp,title,comment)

############## 例5
title="アイテムの階層分類を使った例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more taxo.csv
mitemset.rb S=4 tid=tid item=item i=dat1.csv x=taxo.csv taxo=taxonomy O=result5
more result5/patterns.csv
EOF
run(scp,title,comment)

############## 例6
title="オリジナルアイテムを階層分類で置換する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more taxo.csv
mitemset.rb S=4 tid=tid item=item i=dat1.csv x=taxo.csv taxo=taxonomy -replaceTaxo O=result6
more result6/patterns.csv
EOF
run(scp,title,comment)

############## 例7
title="顕在パターンの列挙例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mitemset.rb S=2 tid=tid item=item class=class i=dat2.csv p=0.6 O=result7
more result7/patterns.csv
EOF
run(scp,title,comment)

