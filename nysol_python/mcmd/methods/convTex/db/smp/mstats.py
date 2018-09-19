# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mstats'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,quantity,amount
A,1,10
B,5,20
B,2,10
C,1,15
C,3,10
C,1,21
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``customer`` 項目を単位に ``quantity`` と ``amount`` 項目の
各統計量合計値を計算する。
'''
script['sh_code']='''
mstats k=顧客 f=数量,金額 c=sum i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mstats(k="customer", f="quantity,amount", c="sum", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='基本例2'
script['comment']='''
各統計量最大値を計算する。
'''
script['sh_code']='''
mstats k=顧客 f=数量,金額 c=max i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mstats(k="customer", f="quantity,amount", c="max", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

