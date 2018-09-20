# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='now'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id
1
2
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mcal c='now()' a=rsl i=dat1.csv o=rsl1-1.csv
mcal c='unow()' a=rsl i=dat1.csv o=rsl1-2.csv
'''
script['py_code']='''
nm.mcal(c='now()', a='rsl', i="dat1.csv", o="rsl1-1.csv").run()
nm.mcal(c='unow()', a='rsl', i="dat1.csv", o="rsl1-2.csv").run()
'''
script['odatas']='rsl1-1.csv'
db['scripts'].append(script)

script={}
script['title']='時刻のみ切り出し'
script['comment']='''
'''
script['sh_code']='''
mcal c='time(now())' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='time(now())', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl1-2.csv'
db['scripts'].append(script)

script={}
script['title']='日付のみ切り出し'
script['comment']='''
'''
script['sh_code']='''
mcal c='date(now())' a=rsl i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='date(now())', a='rsl', i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

