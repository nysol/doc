# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mvnullto'

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
script['title']='nullを文字列nullに置換する例'
script['comment']='''
'''
script['sh_code']='''
mvnullto vf=items v=null i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mvnullto(vf="items", v="null", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='分かりやすく区切り文字を.(ドット)にした例'
script['comment']='''
'''
script['sh_code']='''
mvnullto vf=items v=null delim=. i=dat2.csv o=rsl2.csv
'''
script['py_code']='''
nm.mvnullto(vf="items", v="null", delim=".", i="dat2.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='nullを直前の値に置換する例'
script['comment']='''
'''
script['sh_code']='''
mvnullto vf=items -p i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mvnullto(vf="items", p=True, i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='O=を指定することで、null以外は全て指定の値に置換される'
script['comment']='''
'''
script['sh_code']='''
mvnullto vf=items v=null O=X i=dat1.csv o=rsl4.csv
'''
script['py_code']='''
nm.mvnullto(vf="items", v="null", O="X", i="dat1.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

