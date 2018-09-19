# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mcross'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
item,date,quantity,price
A,20081201,1,10
A,20081202,2,20
A,20081203,3,30
B,20081201,4,40
B,20081203,5,50
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``item`` 項目を単位に ``date`` 項目を横に展開し、
``quantity`` 項目を出力する。
'''
script['sh_code']='''
mcross k=item f=quantity s=date i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcross(k="item", f="quantity", s="date", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='元の入力データに戻す例'
script['comment']='''
例1の出力結果を元に戻すには、同じく ``mcross`` を以下のよう用いればよい。
'''
script['sh_code']='''
mcross k=item f=2008* s=fld a=date i=rsl1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcross(k="item", f="2008*", s="fld", a="date", i="rsl1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='複数の値を出力'
script['comment']='''
``quantity,price`` の2項目を出力する。
'''
script['sh_code']='''
mcross k=item f=quantity,price s=date i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcross(k="item", f="quantity,price", s="date", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='並びを逆順する例'
script['comment']='''
横に展開する項目名の並びを逆順にする。
'''
script['sh_code']='''
mcross k=item f=quantity,price s=date%r i=dat1.csv o=rsl4.csv
'''
script['py_code']='''
nm.mcross(k="item", f="quantity,price", s="date%r", i="dat1.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

