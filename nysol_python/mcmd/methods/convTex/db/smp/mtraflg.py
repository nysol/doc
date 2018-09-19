# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mtraflg'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,egg,milk
A,1,1
B,,1
C,1,
D,1,1
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``egg`` と ``milk`` 項目の値がNULL値以外なら、それら項目名を要素としたベクトルを作成する。
'''
script['sh_code']='''
mtraflg f=egg,milk a=transaction i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mtraflg(f="egg,milk", a="transaction", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='基本例2'
script['comment']='''
出力された結果を ``r=True`` をつけて再実行し元に戻す。
'''
script['sh_code']='''
mtraflg -r f=egg,milk a=transaction i=rsl1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mtraflg(r=True, f="egg,milk", a="transaction", i="rsl1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='区切り文字の指定'
script['comment']='''
区切り文字を-(ハイフン）で連結し、 ``transaction`` という項目名で出力する。
'''
script['sh_code']='''
mtraflg f=egg,milk a=transaction delim=- i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mtraflg(f="egg,milk", a="transaction", delim="-", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

