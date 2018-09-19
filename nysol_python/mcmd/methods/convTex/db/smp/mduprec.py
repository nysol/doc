# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mduprec'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
store,val
A,2
B,
C,5
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``quantity`` 項目の値の数分、データを複写し複数行のデータを生成する。
対象項目がNULL値の場合は複写しない。
'''
script['sh_code']='''
mduprec f=val i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mduprec(f="val", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='複写行数の指定'
script['comment']='''
データを2行づつ複写した( ``n=2`` )データを生成する。
'''
script['sh_code']='''
mduprec n=2 i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mduprec(n="2", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

