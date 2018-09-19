# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='msum'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,quantity,amount
A,1,10
B,1,15
A,2,20
B,3,10
B,1,20
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``customer`` 項目を単位に ``quantity`` と ``amount`` 項目の合計値を計算し、
``qttTotal`` と ``amtTotal`` という項目名で出力する。
'''
script['sh_code']='''
msum k=顧客 f=数量:数量合計,金額:金額合計 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.msum(k="customer", f="quantity:qttTotal,amount:amtTotal", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

