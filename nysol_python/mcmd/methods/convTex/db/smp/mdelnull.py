# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mdelnull'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,quantity,amount
A,1,10
A,,20
B,1,15
B,3,
C,1,20
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
customer,quantity,amount
A,1,10
A,,
B,1,15
B,3,
C,1,20
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``quantity`` と ``amount`` 項目がNULL値の行を削除する。
NULL値の行は ``oth.csv`` に出力する。
'''
script['sh_code']='''
mdelnull f=数量,金額 u=oth.csv i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mdelnull(f="quantity,amount", u="oth.csv", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='oth.csv,rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='NULL値の行を選択'
script['comment']='''
``r=True`` を指定することで、削除ではなく選択することになる。
'''
script['sh_code']='''
mdelnull f=数量,金額 -r i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mdelnull(f="quantity,amount", r=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='キー項目でのNULL値の行の削除'
script['comment']='''
``k=`` を指定することで、集計キー単位で削除することになる。
以下では ``customer`` 項目を単位にして、 ``quantity`` と ``amount`` 項目にNULL値が一つでも含まれていれば削除する。
'''
script['sh_code']='''
mdelnull k=顧客 f=数量,金額 i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mdelnull(k="customer", f="quantity,amount", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='項目間AND条件の例'
script['comment']='''
``quantity`` と ``amount`` 項目の両方がNULL値の行を削除する。
'''
script['sh_code']='''
mdelnull f=数量,金額 -F i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.mdelnull(f="quantity,amount", F=True, i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='レコード間AND条件の例'
script['comment']='''
``customer`` 項目を単位にして、 ``quantity`` 項目が全てNULL値の行を削除する。
'''
script['sh_code']='''
mdelnull k=顧客 f=数量 -R i=dat1.csv o=rsl5.csv
'''
script['py_code']='''
nm.mdelnull(k="customer", f="quantity", R=True, i="dat1.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

