# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mselstr'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
item,amount
apple,100
milk,350
orange,100
pineapplejuice,500
wine,1000
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
customer,item,amount
A,apple,100
A,milk,350
B,orange,100
B,orange,100
B,pineapple,500
B,wine,1000
C,apple,100
C,orange,100
'''
db['idatas'].append(data)

data={}
data['name']='dat3.csv'
data['text']='''
item,amount
果物:柿,100
果物:桃,250
果物:葡萄,300
果物:梨,450
果物:苺,500
'''
db['idatas'].append(data)

data={}
data['name']='dat4.csv'
data['text']='''
customer,item,amount,gender,buyDate,prevBuyDate
A,apple,100,1,2013/01/04,2013/01/01
A,milk,350,1,2013/04/04,2011/05/06
B,orange,100,2,2012/11/11,2011/12/12
B,orange,100,2,2013/05/30,2012/11/11
B,pineapple,500,2,2013/04/15,2013/04/01
B,wine,1000,2,2012/12/24,2011/12/24
C,apple,100,2,2013/02/14,NULL
C,orange,100,2,2013/02/14,2013/01/31
D,orange,100,2,2011/10/28,NULL
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``item`` 項目の値が ``apple、orange`` に完全一致する行を選択し、
``rsl1.csv`` に出力する。
``u=oth1.csv`` を指定すれば、それ以外の行は ``oth1.csv`` に出力する。
``pineapplejuice`` は完全一致ではないので、 ``oth1.csv`` に出力される。
'''
script['sh_code']='''
mselstr f=商品 v=apple,orange u=oth1.csv i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mselstr(f="item", v="apple,orange", u="oth1.csv", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='oth1.csv,rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='行の削除'
script['comment']='''
``r=True`` オプションを指定することで、例1とは逆に、商品項目の値が ``apple、orange`` に完全一致する行を削除し、
``rsl2.csv`` に出力する。
'''
script['sh_code']='''
mselstr f=商品  v=apple,orange -r i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mselstr(f="item", v="apple,orange", r=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='キー単位での選択'
script['comment']='''
``orange`` を購入したことのある顧客を選択する
``k=顧客`` を指定することで、 ``orange`` を購入したことのある顧客の他に購入した商品の行を含めて選択する。
それ以外の行は ``oth2.csv`` に出力する。
'''
script['sh_code']='''
mselstr k=顧客 f=商品 v=orange u=oth2.csv i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mselstr(k="customer", f="item", v="orange", u="oth2.csv", i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='oth2.csv,rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='部分一致'
script['comment']='''
``item`` 項目の値が ``apple`` に部分一致するの行を選択し、
``rsl4.csv`` に出力する。
部分一致であるため ``pine(apple)juice`` も ``rsl4.csv`` に出力される。
'''
script['sh_code']='''
mselstr f=商品 v=apple -sub i=dat1.csv o=rsl4.csv
'''
script['py_code']='''
nm.mselstr(f="item", v="apple", sub=True, i="dat1.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='ワイド文字の部分一致'
script['comment']='''
``item`` 項目の値がワイド文字の「柿」、「桃」、「葡萄」の行を選択(部分一致)
選択項目にワイド文字が使用されている場合にバイト単位のマッチングを使用すると、
マルチバイト文字をまたいだ文字列にマッチングする可能性がある。
その為、ワイド文字が選択項目に含まれる場合は ``W=True`` オプションを使用して、
ワイド文字を使用していることを意図的に示す必要がある。
'''
script['sh_code']='''
mselstr f=商品 v=柿,桃,葡萄 -sub -W i=dat3.csv o=rsl5.csv
'''
script['py_code']='''
nm.mselstr(f="item", v="柿,桃,葡萄", sub=True, W=True, i="dat3.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

script={}
script['title']='商品の購入日と前回の購入日が2013年の商品データを選択'
script['comment']='''
``F=True`` オプションを指定することで、同じ商品を2013年内に購入したことのある(購入日と前回購入日両方が2013年)商品行を選択し、
``rsl6.csv`` に出力する。
それ以外の行は ``oth3.csv`` に出力する。
'''
script['sh_code']='''
mselstr f=購入日,前回購入日 -F -sub v=2013 u=oth3.csv i=dat4.csv o=rsl6.csv
'''
script['py_code']='''
nm.mselstr(f="buyDate,prevBuyDate", F=True, sub=True, v="2013", u="oth3.csv", i="dat4.csv", o="rsl6.csv").run()
'''
script['odatas']='oth3.csv,rsl6.csv'
db['scripts'].append(script)

script={}
script['title']='商品の購入日と前回の購入日が2013年の顧客データの抽出'
script['comment']='''
``k=顧客`` を指定することで、同じ商品を2013年内に購入したことのある顧客の他に購入した商品の行を含めて選択する。
それ以外の行は ``oth4.csv`` に出力する。
'''
script['sh_code']='''
mselstr k=顧客 f=購入日,前回購入日 -F -sub v=2013 u=oth4.csv i=dat4.csv o=rsl7.csv
'''
script['py_code']='''
nm.mselstr(k="customer", f="buyDate,prevBuyDate", F=True, sub=True, v="2013", u="oth4.csv", i="dat4.csv", o="rsl7.csv").run()
'''
script['odatas']='oth4.csv,rsl7.csv'
db['scripts'].append(script)

script={}
script['title']='2013年度の新規顧客情報の抽出'
script['comment']='''
``R=True`` オプションを指定することで、購入日、前回購入日両方が2013年,NULL(前回購入なし)の顧客情報を抽出する。
つまり2013年の新規顧客データを選択し、 ``rsl8.csv`` に出力する。
それ以外の行は  ``oth5.csv`` に出力する。
'''
script['sh_code']='''
mselstr k=顧客 f=購入日,前回購入日 -F -R -sub v=2013,NULL u=oth5.csv i=dat4.csv o=rsl8.csv
'''
script['py_code']='''
nm.mselstr(k="customer", f="buyDate,prevBuyDate", F=True, R=True, sub=True, v="2013,NULL", u="oth5.csv", i="dat4.csv", o="rsl8.csv").run()
'''
script['odatas']='oth5.csv,rsl8.csv'
db['scripts'].append(script)

