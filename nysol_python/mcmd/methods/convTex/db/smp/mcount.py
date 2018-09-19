# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mcount'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
date
20090109
20090109
20090110
20090109
20090110
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``date`` 項目を単位に行数をカウントし、 ``count`` という項目名で出力する。
'''
script['sh_code']='''
mcount k=date a=count i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcount(k="date", a="count", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='集計キーなし'
script['comment']='''
集計キーを指定しなければ全体の行数をカウントする。
'''
script['sh_code']='''
mcount a=count i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcount(a="count", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

