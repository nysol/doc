# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='line'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id
1
2
3
4
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
0から始まる番号が出力される。
'''
script['sh_code']='''
mcal c='line()' a=no i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='line()', a='no', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='1から始める'
script['comment']='''
1から始まる番号を出力する。
'''
script['sh_code']='''
mcal c='line()+1' a=no i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='line()+1', a='no', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

