# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='msortf'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
item,date,quantity,price
B,20081201,4,40
A,20081201,10,200
A,20081201,10,100
B,20081203,5,50
B,20081201,2,500
A,20081201,3,300
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``item、date`` 順に並べ替える。
'''
script['sh_code']='''
msortf f=item,date i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.msortf(f="item,date", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='数量(quantity)降順，金額(price)昇順に並べ替える例'
script['comment']='''
'''
script['sh_code']='''
msortf f=quantity%nr,price%n i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.msortf(f="quantity%nr,price%n", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

