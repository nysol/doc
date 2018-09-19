# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mvuniq'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
items1,items2
b a c,1 1
c c,2 2 3
e a a,3 1
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='複数項目を単一化する例'
script['comment']='''
'''
script['sh_code']='''
mvuniq vf=items1,items2 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mvuniq(vf="items1,items2", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

