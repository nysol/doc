# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='muniq'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
date,customer
20081201,A
20081202,A
20081202,B
20081202,B
20081203,C
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``date`` 項目を単位に重複行を削除し単一にする。
'''
script['sh_code']='''
muniq k=date i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.muniq(k="date", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='複数の項目での重複行の削除'
script['comment']='''
``date`` と ``customer`` 項目を単位に重複行を削除し単一にする。
'''
script['sh_code']='''
muniq k=date,customer i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.muniq(k="date,customer", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

