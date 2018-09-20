# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='not'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,b
1,1
2,
3,0
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mcal c='not($b{b})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='not($b{b})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

