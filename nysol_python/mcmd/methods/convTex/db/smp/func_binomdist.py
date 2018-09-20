# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='binomdist'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
k,n,p
0,2,0.5
1,2,0.5
2,2,0.5
4,10,0.2
40,100,0.2
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mcal c='binomdist(${k},${n},${p})' a=prob i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='binomdist(${k},${n},${p})', a='prob', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

