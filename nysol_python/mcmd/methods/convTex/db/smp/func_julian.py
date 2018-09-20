# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='julian'

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
日付型の ``date`` 項目を ``julian`` 関数でユリウス通日に変換し、 ``julian2d`` 関数でまたもとに戻す。
'''
script['sh_code']='''
mcal c='julian($d{date})' a=julian i=dat1.csv o=rsl1.csv
mcal c='julian2d(${julian})' a=date2 i=rsl1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='julian($d{date})', a='julian', i="dat1.csv", o="rsl1.csv").run()
nm.mcal(c='julian2d(${julian})', a='date2', i="rsl1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='時刻型も同様'
script['comment']='''
'''
script['sh_code']='''
mcal c='julian($t{time})' a=julian i=dat2.csv o=rsl3.csv
mcal c='julian2t(${julian})' a=time2 i=rsl3.csv o=rsl4.csv
'''
script['py_code']='''
nm.mcal(c='julian($t{time})', a='julian', i="dat2.csv", o="rsl3.csv").run()
nm.mcal(c='julian2t(${julian})', a='time2', i="rsl3.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

