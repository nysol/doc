# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='month'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,date
1,20000101
2,20121021
3,
4,19770812
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,time
1,20000101000000
2,20121021111213
3,
4,19770812122212
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mcal c='month($d{date})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='month($d{date})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='固定長文字列として'
script['comment']='''
'''
script['sh_code']='''
mcal c='months($d{date})' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='months($d{date})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='英語表記'
script['comment']='''
'''
script['sh_code']='''
mcal c='monthe($d{date})' a=rsl i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='monthe($d{date})', a='rsl', i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='英語短縮表記'
script['comment']='''
'''
script['sh_code']='''
mcal c='monthes($d{date})' a=rsl i=dat1.csv o=rsl4.csv
'''
script['py_code']='''
nm.mcal(c='monthes($d{date})', a='rsl', i="dat1.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='時刻型でも可能'
script['comment']='''
'''
script['sh_code']='''
mcal c='month($t{time})' a=rsl i=dat2.csv o=rsl5.csv
'''
script['py_code']='''
nm.mcal(c='month($t{time})', a='rsl', i="dat2.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

