# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='maccum'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,quantity,amount
A,1,10
A,2,20
B,1,15
B,3,10
B,1,20
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
customer,quantity,amount
A,1,10
A,,20
B,1,15
B,3,
B,1,20
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``quantity`` と ``amount`` 項目の累積値を計算し、 ``qttAccum`` と ``amtAccum`` という項目名で出力する。
'''
script['sh_code']='''
maccum s=顧客 f=数量:数量累計,金額:金額累計 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.maccum(s="customer", f="quantity:qttAccum,amount:amtAccum", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='キー項目を指定する例'
script['comment']='''
``customer`` 項目を単位に ``quantity`` と ``amount`` 項目の累積値を計算し、 ``qttAccum`` と ``amtAccum`` という項目名で出力する。
'''
script['sh_code']='''
maccum k=顧客 s=顧客 f=数量:数量累計,金額:金額累計 i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.maccum(k="customer", s="customer", f="quantity:qttAccum,amount:amtAccum", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='NULL値を含む累計'
script['comment']='''
``quantity`` と ``amount`` 項目の累積値を計算し、 ``qttAccum`` と ``amtAccum`` という項目名で出力する。
NULLは無視される。結果もNULLが出力される。
'''
script['sh_code']='''
maccum s=顧客 f=数量:数量累計,金額:金額累計 i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.maccum(s="customer", f="quantity:qttAccum,amount:amtAccum", i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

