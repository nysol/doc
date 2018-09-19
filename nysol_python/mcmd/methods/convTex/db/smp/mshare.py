# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mshare'

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

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``customer`` 項目を単位に ``quantity`` と ``amount`` 項目のシェアを計算し、
「数量シェア」と「金額シェア」という項目名で出力する。
'''
script['sh_code']='''
mshare k=顧客 f=数量:数量シェア,金額:金額シェア i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mshare(k="customer", f="quantity:quantityシェア,amount:amountシェア", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

