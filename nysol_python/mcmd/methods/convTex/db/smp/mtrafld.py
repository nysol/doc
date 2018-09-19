# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mtrafld'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,price,quantity
A,198,1
B,325,2
C,200,3
D,450,2
E,100,1
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
customer,price,quantity
A,198,1
B,,2
C,200,
D,450,2
E,,
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``price`` と ``quantity`` 項目を1つの文字列として連結し、
``transaction`` という項目名で出力する。
'''
script['sh_code']='''
mtrafld a=transaction f=price,quantity i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mtrafld(a="transaction", f="price,quantity", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='基本例2'
script['comment']='''
出力された結果を ``r=True`` をつけて再実行し元に戻す。
'''
script['sh_code']='''
mtrafld -r a=transaction f=price,quantity i=rsl1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mtrafld(r=True, a="transaction", f="price,quantity", i="rsl1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='区切り文字の指定'
script['comment']='''
``price`` と数量 ``quantity`` 項目を\_(アンダーバー）で区切り1つの文字列として連結し、
項目名とデータは：（コロン）で区切り ``transaction`` という項目名で出力する。
'''
script['sh_code']='''
mtrafld a=transaction f=price,quantity delim=_ delim2=':' i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mtrafld(a="transaction", f="price,quantity", delim="_", delim2=":", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='NULL値を含む場合'
script['comment']='''
'''
script['sh_code']='''
mtrafld a=transaction f=price,quantity i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.mtrafld(a="transaction", f="price,quantity", i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='NULL値を含む場合2'
script['comment']='''
出力された結果を ``r=True`` をつけて再実行し元に戻す。
'''
script['sh_code']='''
mtrafld -r a=transaction f=price,quantity i=rsl4.csv o=rsl5.csv
'''
script['py_code']='''
nm.mtrafld(r=True, a="transaction", f="price,quantity", i="rsl4.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

script={}
script['title']='-valOnlyの指定'
script['comment']='''
'''
script['sh_code']='''
mtrafld -valOnly f=price,quantity a=transaction i=dat2.csv o=rsl6.csv
'''
script['py_code']='''
nm.mtrafld(valOnly=True, f="price,quantity", a="transaction", i="dat2.csv", o="rsl6.csv").run()
'''
script['odatas']='rsl6.csv'
db['scripts'].append(script)

