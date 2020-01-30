#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
商品,金額
apple,100
milk,350
orange,100
pineapplejuice,500
wine,1000
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,商品,金額
A,apple,100
A,milk,350
B,orange,100
B,orange,100
B,pineapple,500
B,wine,1000
C,apple,100
C,orange,100
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
商品,金額
果物:柿,100
果物:桃,250
果物:葡萄,300
果物:梨,450
果物:苺,500
EOF
)}

File.open("dat4.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,商品,金額,性別,購入日,前回購入日
A,apple,100,1,2013/01/04,2013/01/01
A,milk,350,1,2013/04/04,2011/05/06
B,orange,100,2,2012/11/11,2011/12/12
B,orange,100,2,2013/05/30,2012/11/11
B,pineapple,500,2,2013/04/15,2013/04/01
B,wine,1000,2,2012/12/24,2011/12/24
C,apple,100,2,2013/02/14,NULL
C,orange,100,2,2013/02/14,2013/01/31
D,orange,100,2,2011/10/28,NULL
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
「商品」項目の値が\verb|apple、orange|に完全一致する行を選択し、
\verb|rsl1.csv|に出力する。
\verb|u=oth1.csv|を指定すれば、それ以外の行は\verb|oth1.csv|に出力する。
\verb|pineapplejuice|は完全一致ではないので、\verb|oth1.csv|に出力される。
EOF
scp=<<'EOF'
more dat1.csv
mselstr f=商品 v=apple,orange u=oth1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
more oth1.csv
EOF
run(scp,title,comment)

############## 例2
title="行の削除"
comment=<<'EOF'
\verb|-r|オプションを指定することで、例1とは逆に、商品項目の値が\verb|apple、orange|に完全一致する行を削除し、
\verb|rsl2.csv|に出力する。
EOF
scp=<<'EOF'
mselstr f=商品  v=apple,orange -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="キー単位での選択"
comment=<<'EOF'
\verb|orange|を購入したことのある顧客を選択する
\verb|k=顧客|を指定することで、\verb|orange|を購入したことのある顧客の他に購入した商品の行を含めて選択する。
それ以外の行は\verb|oth2.csv|に出力する。
EOF
scp=<<'EOF'
more dat2.csv
mselstr k=顧客 f=商品 v=orange u=oth2.csv i=dat2.csv o=rsl3.csv
more rsl3.csv
more oth2.csv
EOF
run(scp,title,comment)

############## 例4
title="部分一致"
comment=<<'EOF'
「商品」項目の値が\verb|apple|に部分一致するの行を選択し、
\verb|rsl4.csv|に出力する。
部分一致であるため\verb|pine(apple)juice|も\verb|rsl4.csv|に出力される。
EOF
scp=<<'EOF'
mselstr f=商品 v=apple -sub i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="ワイド文字の部分一致"
comment=<<'EOF'
「商品」項目の値がワイド文字の「柿」、「桃」、「葡萄」の行を選択(部分一致)
選択項目にワイド文字が使用されている場合にバイト単位のマッチングを使用すると、
マルチバイト文字をまたいだ文字列にマッチングする可能性がある。
その為、ワイド文字が選択項目に含まれる場合は\verb|-W|オプションを使用して、
ワイド文字を使用していることを意図的に示す必要がある。
EOF
scp=<<'EOF'
more dat3.csv
mselstr f=商品 v=柿,桃,葡萄 -sub -W i=dat3.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## 例6
title="商品の購入日と前回の購入日が2013年の商品データを選択"
comment=<<'EOF'
\verb|-F|オプションを指定することで、同じ商品を2013年内に購入したことのある(購入日と前回購入日両方が2013年)商品行を選択し、
\verb|rsl6.csv|に出力する。
それ以外の行は\verb|oth3.csv|に出力する。
EOF
scp=<<'EOF'
more dat4.csv
mselstr f=購入日,前回購入日 -F -sub v=2013 u=oth3.csv i=dat4.csv o=rsl6.csv
more rsl6.csv
more oth3.csv
EOF
run(scp,title,comment)

############## 例7
title="商品の購入日と前回の購入日が2013年の顧客データの抽出"
comment=<<'EOF'
\verb|k=顧客|を指定することで、同じ商品を2013年内に購入したことのある顧客の他に購入した商品の行を含めて選択する。
それ以外の行は\verb|oth4.csv|に出力する。
EOF
scp=<<'EOF'
mselstr k=顧客 f=購入日,前回購入日 -F -sub v=2013 u=oth4.csv i=dat4.csv o=rsl7.csv
more rsl7.csv
more oth4.csv
EOF
run(scp,title,comment)

############## 例8
title="2013年度の新規顧客情報の抽出"
comment=<<'EOF'
\verb|-R|オプションを指定することで、購入日、前回購入日両方が2013年,NULL(前回購入なし)の顧客情報を抽出する。
つまり2013年の新規顧客データを選択し、\verb|rsl8.csv|に出力する。
それ以外の行は \verb|oth5.csv|に出力する。
EOF
scp=<<'EOF'
mselstr k=顧客 f=購入日,前回購入日 -F -R -sub v=2013,NULL u=oth5.csv i=dat4.csv o=rsl8.csv
more rsl8.csv
more oth5.csv
EOF
run(scp,title,comment)
