# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='msetstr'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,date
A,20081202
A,20081204
B,20081203
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
日付計算で必要となる基準日を(2007年01月01日と定義した場合)すべての行に「 ``20070101`` 」という文字列を追加し「基準日」という項目名で出力する。
'''
script['sh_code']='''
msetstr v=20070101 a=基準日 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.msetstr(v="20070101", a="基準日", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='複数項目を追加'
script['comment']='''
'''
script['sh_code']='''
msetstr v=20070101,20070201 a=基準日1,基準日2 i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.msetstr(v="20070101,20070201", a="基準日1,基準日2", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='null値項目追加'
script['comment']='''
'''
script['sh_code']='''
msetstr v= a=追加項目 i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.msetstr(v="", a="追加項目", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

