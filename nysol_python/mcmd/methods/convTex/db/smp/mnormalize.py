# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mnormalize'

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
``customer`` を単位にして ``quantity`` と ``amount`` 項目を基準化（z得点）し、
``qttNorm`` と ``amtNorm`` という項目名で出力する。
'''
script['sh_code']='''
mnormalize c=z k=顧客 f=数量:数量基準値,金額:金額基準値 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mnormalize(c="z", k="customer", f="quantity:qttNorm,amount:amtNorm", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='偏差値'
script['comment']='''
'''
script['sh_code']='''
mnormalize c=Z k=顧客 f=数量:数量基準値,金額:金額基準値 i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mnormalize(c="Z", k="customer", f="quantity:qttNorm,amount:amtNorm", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='0から1への線形変換'
script['comment']='''
'''
script['sh_code']='''
mnormalize c=range k=顧客 f=数量:数量基準値,金額:金額基準値 i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mnormalize(c="range", k="customer", f="quantity:qttNorm,amount:amtNorm", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

