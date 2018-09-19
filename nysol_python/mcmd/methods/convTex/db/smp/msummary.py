# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='msummary'

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
``customer`` 項目を単位に ``quantity`` と ``amount`` 項目の中央値・平均値を求める。
統計量を求めた項目名は「変数」という項目に出力する。
'''
script['sh_code']='''
msummary k=顧客 f=数量,金額 c=median:中央値,mean:平均値 a=変数 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.msummary(k="customer", f="quantity,amount", c="median:中央値,mean:平均値", a="変数", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

