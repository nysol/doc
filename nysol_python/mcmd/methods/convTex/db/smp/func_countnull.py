# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='countnull'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
a,b,c,d
1,,3,4
1,,,
,,,
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mcal c='countnull(${a},${b},${c},${d})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='countnull(${a},${b},${c},${d})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='他の項目型として項目名をワイルドカードで指定'
script['comment']='''
'''
script['sh_code']='''
mcal c='countnull($s{*})' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='countnull($s{*})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

