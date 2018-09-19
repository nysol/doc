# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mproduct'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer
A
B
'''
db['idatas'].append(data)

data={}
data['name']='ref1.csv'
data['text']='''
date
20090101
20090201
20090301
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
入力ファイルにある ``customer`` 項目に対して、
参照ファイルにある ``date`` 項目全行を結合する。
'''
script['sh_code']='''
mproduct f=date m=ref1.csv i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mproduct(f="date", m="ref1.csv", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

