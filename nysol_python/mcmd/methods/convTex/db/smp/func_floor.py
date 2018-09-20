# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='floor'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,val
1,3.28
2,3.82
3,
4,-0.6
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,val
1,1341.28
2,188
3,1.235E+3
4,-1.235E+3
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
小数点以下一桁目を切り捨てる。
'''
script['sh_code']='''
mcal c='floor(${val})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='floor(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='基本例'
script['comment']='''
小数点以下二桁目を切り捨てる。
'''
script['sh_code']='''
mcal c='floor(${val},0.1)' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='floor(${val},0.1)', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='基数0.5の例'
script['comment']='''
0.5を基数として切り捨てる。
'''
script['sh_code']='''
mcal c='floor(${val},0.5)' a=rsl i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='floor(${val},0.5)', a='rsl', i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='基数10の例'
script['comment']='''
一桁目を切り捨てる。
'''
script['sh_code']='''
mcal c='floor(${val},10)' a=rsl i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.mcal(c='floor(${val},10)', a='rsl', i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

