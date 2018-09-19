# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mnjoin'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
item,date,price
A,20081201,100
A,20081213,98
B,20081002,400
B,20081209,450
C,20081201,100
'''
db['idatas'].append(data)

data={}
data['name']='ref1.csv'
data['text']='''
item,cost
A,50
A,70
B,300
E,200
'''
db['idatas'].append(data)

data={}
data['name']='ref2.csv'
data['text']='''
item,cost
A,50
B,300
E,200
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
入力ファイルにある ``item`` 項目と、
参照ファイルにある ``item`` 項目を比較し同じ値の場合、 ``cost`` 項目を結合する。
入力ファイル、参照ファイル共に ``item=A`` が2行あり、結果、出力ファイルには2$\times$2=4行の ``item=A`` が出力されている。
'''
script['sh_code']='''
mnjoin k=item f=cost m=ref1.csv i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mnjoin(k="item", f="cost", m="ref1.csv", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='未結合データ出力'
script['comment']='''
``n=True`` を指定することで、参照ファイルにマッチしない入力ファイルの行( ``item="C"`` の行)も出力し、
``N=True`` を指定することで、入力ファイルにマッチしない参照ファイルの行( ``item="E"`` の行)も出力する。
'''
script['sh_code']='''
mnjoin k=item f=cost m=ref2.csv -n -N i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mnjoin(k="item", f="cost", m="ref2.csv", n=True, N=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

