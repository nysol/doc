# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mbucket'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,x,y
A,2,7
B,6,7
C,5,6
D,7,5
E,6,4
F,1,3
G,3,3
H,4,2
I,7,2
J,2,1
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,x,y
A,2,7
A,6,7
A,5,6
B,7,5
B,6,4
B,1,3
C,3,3
C,4,2
C,7,2
C,2,1
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``x,y`` 項目それぞれで、件数ができるだけ均等になるように2分割する。
その際、各バケットの数値範囲を ``rng1.csv`` に出力する。
'''
script['sh_code']='''
mbucket f=x:xb,y:yb n=2 O=rng1.csv i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mbucket(f="x:xb,y:yb", n="2", O="rng1.csv", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='範囲均等化分割'
script['comment']='''
``rng=True`` オプションを指定すると範囲均等化分割となる。
'''
script['sh_code']='''
mbucket f=x:xb,y:yb n=2 -rng O=rng2.csv i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mbucket(f="x:xb,y:yb", n="2", rng=True, O="rng2.csv", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='キー項目を指定した例'
script['comment']='''
id項目を集計キーとして、 ``x,y`` 項目それぞれを件数均等化バケット分割する。
``n=2,3`` と指定することで、 ``x`` 項目の分割数は2に、
``y`` 項目の分割数は3となる。
出力形式はバケット番号とバケット範囲の両方を表示する( ``F=2`` )。
'''
script['sh_code']='''
mbucket k=id f=x:xb,y:yb n=2,3 F=2 i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mbucket(k="id", f="x:xb,y:yb", n="2,3", F="2", i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

