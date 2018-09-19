# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mhashsum'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,quantity,amount
A,1,
B,,15
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
``customer`` 項目を単位にして、 ``quantity`` と ``amount`` 項目の合計を計算する。
'''
script['sh_code']='''
mhashsum k=顧客 f=数量,金額 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mhashsum(k="customer", f="quantity,amount", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='NULL値出力'
script['comment']='''
``n=True`` オプションを指定することで、NULL値が含まれている場合は、結果もNULL値として出力する。
'''
script['sh_code']='''
mhashsum k=顧客 f=数量,金額 -n i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mhashsum(k="customer", f="quantity,amount", n=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

