# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='diff'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,date
1,19641010
2,20000101
3,20130831
4,20130901
5,20130902
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,time
1,20120101000000
2,20120101011112
3,
4,20111231235000
5,20111231235000.123456
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='月単位での期間'
script['comment']='''
``date`` 項目から2013年9月1日までの経過期間を日数で計算する。
'''
script['sh_code']='''
mcal c='diffday(0d20130901,$d{date})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='diffday(0d20130901,$d{date})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='分単位での期間'
script['comment']='''
``time`` 項目から2012年1月1日 00時00分00秒までの経過期間を分単位で計算する。
'''
script['sh_code']='''
mcal c='diffmonth(0t20120101000000,$t{time})' a=rsl i=dat2.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='diffmonth(0t20120101000000,$t{time})', a='rsl', i="dat2.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='マイクロ秒単位での期間'
script['comment']='''
``time`` 項目から2012年1月1日 00時00分00秒までの経過期間を秒単位およびマイクロ秒単位で計算する。
'''
script['sh_code']='''
mcal c='diffsecond(0t20120101000000,$t{time})' a=rsl i=dat2.csv o=rsl3.csv
mcal c='diffusecond(0t20120101000000,$t{time})' a=rsl i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.mcal(c='diffsecond(0t20120101000000,$t{time})', a='rsl', i="dat2.csv", o="rsl3.csv").run()
nm.mcal(c='diffusecond(0t20120101000000,$t{time})', a='rsl', i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

