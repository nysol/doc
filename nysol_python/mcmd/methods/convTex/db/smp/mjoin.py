# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mjoin'

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
'''
script['sh_code']='''
mjoin k=item f=cost m=ref1.csv i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mjoin(k="item", f="cost", m="ref1.csv", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='未結合データ出力'
script['comment']='''
入力ファイルにある ``item`` 項目と、
参照ファイルにある ``item`` 項目を比較し同じ値の場合、 ``cost`` 項目を結合する。
その際、参照データにない入力データと参照データにない範囲データをNULL値として出力する。
'''
script['sh_code']='''
mjoin k=item f=cost m=ref1.csv -n -N i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mjoin(k="item", f="cost", m="ref1.csv", n=True, N=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

