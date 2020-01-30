#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,123456789
2,1234.56789
3,0.123456789
4,0.000123456789
5,0.0000123456789
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
id=1は指数表現で1.2345678e+08であり、指数部が有効桁数6を超えているので指数表記となり、仮数部の有効桁数が6となっている。
id=2は指数表現で1.23456789e+03であり、指数部が有効桁数7を超えていないので標準標記となり、整数部+小数部の桁数が6となっている。
id=4は指数表現で1.23456789e-04であり、指数部が-4未満ではないので標準標記となり、有効桁数が6となっている。
id=5は指数表現で1.23456789e-05であり、指数部が-4未満となるため指数表記となり、仮数部の有効桁数が6となっている。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='${val}' a=result precision=6 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="presicion=2の場合"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='${val}' a=result precision=2 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="環境変数による指定"
comment=<<'EOF'
環境変数によって設定すると、それ以降全てのコマンドがその設定値を使う。
EOF
scp=<<'EOF'
export KG_Precision=4
mcal c='${val}' a=result i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

