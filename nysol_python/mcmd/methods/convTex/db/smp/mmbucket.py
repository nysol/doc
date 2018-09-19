# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mmbucket'

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
``x、y`` 項目の件数ができるだけ多次元均等になるように2分割する。
その際、各バケットの数値範囲を ``rng.csv`` という名前のファイルに出力する。
'''
script['sh_code']='''
mmbucket f=x:xb,y:yb n=2,2 O=rng.csv i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mmbucket(f="x:xb,y:yb", n="2,2", O="rng.csv", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='出力形式'
script['comment']='''
``id`` 項目を単位に件数ができるだけ多次元均等になるように ``x,y`` 項目を2分割する。
出力形式はバケット番号とバケット範囲の両方を表示する。
'''
script['sh_code']='''
mmbucket k=id f=x:xb,y:yb n=2,2 F=2 i=dat2.csv o=rsl2.csv
'''
script['py_code']='''
nm.mmbucket(k="id", f="x:xb,y:yb", n="2,2", F="2", i="dat2.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

