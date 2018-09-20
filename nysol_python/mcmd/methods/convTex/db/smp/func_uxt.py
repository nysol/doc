# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='uxt'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,date
1,20000101
2,20121021
3,
4,19700101
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,time
1,20000101000000
2,20121021111213
3,
4,19700101000100
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
日付型の ``date`` 項目を ``uxt`` 関数でUNIX時刻に変換し、 ``uxt2d`` 関数でまたもとに戻す。
'''
script['sh_code']='''
mcal c='uxt($d{date})' a=uxt i=dat1.csv o=rsl1.csv
mcal c='uxt2d(${uxt})' a=date2 i=rsl1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='uxt($d{date})', a='uxt', i="dat1.csv", o="rsl1.csv").run()
nm.mcal(c='uxt2d(${uxt})', a='date2', i="rsl1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='時刻型も同様'
script['comment']='''
'''
script['sh_code']='''
mcal c='uxt($t{time})' a=uxt i=dat2.csv o=rsl3.csv
mcal c='uxt2t(${uxt})' a=time2 i=rsl3.csv o=rsl4.csv
'''
script['py_code']='''
nm.mcal(c='uxt($t{time})', a='uxt', i="dat2.csv", o="rsl3.csv").run()
nm.mcal(c='uxt2t(${uxt})', a='time2', i="rsl3.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

