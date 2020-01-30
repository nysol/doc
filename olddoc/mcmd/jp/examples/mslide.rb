#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
date,val
20130406,1
20130407,2
20130408,3
20130409,4
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mslide s=date f=val:newVal i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="逆にずらした例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mslide s=date f=val:newVal -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="複数回指定した場合"
comment=<<'EOF'
EOF
scp=<<'EOF'
mslide s=date f=val t=2 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="最後にずらした項目だけを出力する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mslide s=date f=val t=2 -l i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="複数項目名を変更して出力する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
mslide s=date f=date:d_,val:v_ t=2 i=dat1.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)
