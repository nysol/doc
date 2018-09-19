# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mcut'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,quantity,amount
A,1,10
A,2,20
B,1,15
B,3,10
B,1,20
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
A,1,10
A,2,20
B,1,15
B,3,10
B,1,20
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``customer`` と ``amount`` 項目を選択する。ただし、 ``amount`` 項目は ``sales`` と名前を変更して出力している。
'''
script['sh_code']='''
mcut f=顧客,金額:売上 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcut(f="customer,amount:sales", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='項目削除'
script['comment']='''
``r=True`` を指定することで、項目を削除できる。
'''
script['sh_code']='''
mcut f=顧客,金額 -r i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcut(f="customer,amount", r=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='項目名なしデータ'
script['comment']='''
ヘッダなし入力ファイルから、0,2番目の項目を選択し、
``customer`` と ``amount`` という名前で出力する。
'''
script['sh_code']='''
mcut f=0:顧客,2:金額 -nfni i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcut(f="0:customer,2:amount", nfni=True, i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

