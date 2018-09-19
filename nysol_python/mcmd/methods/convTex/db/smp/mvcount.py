# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mvcount'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
items1,items2
b a c,b
c c,
e a a,a a a
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='複数項目に対して適用する例'
script['comment']='''
'''
script['sh_code']='''
mvcount vf=items1:size1,items2:size2 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mvcount(vf="items1:size1,items2:size2", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

