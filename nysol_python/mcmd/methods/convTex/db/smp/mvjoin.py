# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mvjoin'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
items
b a c
c c
e a a
'''
db['idatas'].append(data)

data={}
data['name']='ref1.csv'
data['text']='''
item,taxo
a,X Y
b,X
c,Z Z
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
items1,items2
b a c,b b
c c,a d
e a a,a a
'''
db['idatas'].append(data)

data={}
data['name']='ref2.csv'
data['text']='''
item,taxo
a,X
b,X
c,Y
d,Y
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='ベクトルを結合する例'
script['comment']='''
'''
script['sh_code']='''
mvjoin vf=items K=item m=ref1.csv f=taxo i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mvjoin(vf="items", K="item", m="ref1.csv", f="taxo", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='複数項目に対して適用する例'
script['comment']='''
'''
script['sh_code']='''
mvjoin vf=items1,items2 K=item m=ref2.csv f=taxo i=dat2.csv o=rsl2.csv
'''
script['py_code']='''
nm.mvjoin(vf="items1,items2", K="item", m="ref2.csv", f="taxo", i="dat2.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

