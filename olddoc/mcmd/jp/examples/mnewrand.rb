#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
実数乱数を10行生成する。乱数の種は1に固定しているので、いつ実行しても乱数系列は同じになる。
EOF
scp=<<'EOF'
mnewrand a=rand S=1 o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="整数乱数"
comment=<<'EOF'
最小値が0、最大値が1000、乱数の種が1の整数乱数を5行作成する。
EOF
scp=<<'EOF'
mnewrand a=rand -int max=1000 min=0 l=5 S=1 o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="ヘッダ行なしで出力"
comment=<<'EOF'
\verb|-nfn|でヘッダーなしのデータが生成される。
EOF
scp=<<'EOF'
mnewrand -nfn l=5 S=1 o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
