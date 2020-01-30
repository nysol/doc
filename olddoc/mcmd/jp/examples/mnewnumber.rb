#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
1から始まる間隔が1の連番をふり、\verb|No.|という項目名で新規に5行のデータを作成する。
EOF
scp=<<'EOF'
mnewnumber a=No. I=1 S=1 l=5 o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="開始番号と間隔の変更"
comment=<<'EOF'
10から始まる間隔が5の連番をふり、\verb|No.|という項目名で新規に5行のデータを作成する。
EOF
scp=<<'EOF'
mnewnumber a=No. I=5 S=10 l=5 o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="アルファベット連番"
comment=<<'EOF'
Aから始まる間隔が1のアルファベット連番をふり、\verb|No.|という項目名で新規に5行のデータを作成する。
EOF
scp=<<'EOF'
mnewnumber a=No. I=1 S=A l=5 o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="ヘッダ行なしで新規作成"
comment=<<'EOF'
Bから始まる間隔が3のアルファベット連番をふり、ヘッダなしで新規に11行のデータを作成する。
EOF
scp=<<'EOF'
mnewnumber  -nfn  I=3 l=11 S=B o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
