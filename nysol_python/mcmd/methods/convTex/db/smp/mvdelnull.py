# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mvdelnull'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
items
b a  c
c c
e a   b
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
items
b.a..c
.c.c
e.a...b.
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='nullを削除する基本例'
script['comment']='''
'''
script['sh_code']='''
mvdelnull vf=items i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mvdelnull(vf="items", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='分かりやすく区切り文字を.(ドット)にした例'
script['comment']='''
'''
script['sh_code']='''
mvdelnull vf=items delim=. i=dat2.csv o=rsl2.csv
'''
script['py_code']='''
nm.mvdelnull(vf="items", delim=".", i="dat2.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='項目名を変更して出力'
script['comment']='''
'''
script['sh_code']='''
mvdelnull vf=items:new i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mvdelnull(vf="items:new", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='-Aを指定することで追加項目として出力'
script['comment']='''
'''
script['sh_code']='''
mvdelnull vf=items:new -A i=dat1.csv o=rsl4.csv
'''
script['py_code']='''
nm.mvdelnull(vf="items:new", A=True, i="dat1.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

