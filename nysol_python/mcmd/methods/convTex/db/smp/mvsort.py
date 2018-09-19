# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mvsort'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
items1,items2
b a c,10 2
c c,2 5 3
e a a,1
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='複数項目を並べる例'
script['comment']='''
``item1`` 項目を文字列降順に並べ、 ``item2`` 項目を数値昇順に並べる。
'''
script['sh_code']='''
mvsort vf=items1%r,items2%n i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mvsort(vf="items1%r,items2%n", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

