# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mselnum'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,val
1,5.1
2,5
3,-2.0
4,
5,2.0
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``val`` 項目が2以上5以下の行、すなわち ``id=2,5`` の行を選択する。
'''
script['sh_code']='''
mselnum f=val c='[2,5]' i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mselnum(f="val", c="[2,5]", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='片側範囲'
script['comment']='''
``val`` 項目が2以上の行、すなわち ``id=1,2,5`` の行を選択する。
'''
script['sh_code']='''
mselnum f=val c='[2,]' i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mselnum(f="val", c="[2,]", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

