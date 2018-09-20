# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='null'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id
1
2
3
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,val
1,a
2,
3,b
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
rslという項目の全行にNULL値を出力する。
'''
script['sh_code']='''
mcal c='nulls()' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='nulls()', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='if文の中での利用'
script['comment']='''
if文の第二パラメータで数値を指定しているので、それに合わせてnulln()関数を用いる。
'''
script['sh_code']='''
mcal c='if(${id}==1,1,nulln())' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='if(${id}==1,1,nulln())', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='isnullと同等の指定'
script['comment']='''
'''
script['sh_code']='''
mcal c='if(${val}==nulln(),"null","notNull")' a=rsl i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='if(${val}==nulln(),"null","notNull")', a='rsl', i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

