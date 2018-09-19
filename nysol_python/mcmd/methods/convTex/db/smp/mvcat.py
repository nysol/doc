# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mvcat'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
items1,items2,items3,items4
b a c,b,x,y
c c,,x,y
e a a,a a a,x,y
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='ワイルドカードを利用した例'
script['comment']='''
'''
script['sh_code']='''
mvcat vf=items* a=items i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mvcat(vf="items*", a="items", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

