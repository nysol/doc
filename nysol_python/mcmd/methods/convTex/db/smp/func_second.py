# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='second'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,time
1,20000101121103
2,20121021111209.123
3,211209
4,211209.123
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mcal c='second($t{time})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='second($t{time})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='文字列とし出力'
script['comment']='''
'''
script['sh_code']='''
mcal c='seconds($t{time})' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='seconds($t{time})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='マイクロ秒を出力'
script['comment']='''
'''
script['sh_code']='''
mcal c='usecond($t{time})' a=rsl i=dat1.csv o=rsl3.csv
mcal c='useconds($t{time})' a=rsl i=dat1.csv o=rsl4.csv
'''
script['py_code']='''
nm.mcal(c='usecond($t{time})', a='rsl', i="dat1.csv", o="rsl3.csv").run()
nm.mcal(c='useconds($t{time})', a='rsl', i="dat1.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

