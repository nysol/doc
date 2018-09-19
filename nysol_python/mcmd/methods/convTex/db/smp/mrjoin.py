# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mrjoin'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
price
8
15
35
50
90
200
'''
db['idatas'].append(data)

data={}
data['name']='ref1.csv'
data['text']='''
range,category
10,low
35,middle
80,high
100,
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
item,price
A,10
A,20
B,10
B,20
'''
db['idatas'].append(data)

data={}
data['name']='ref2.csv'
data['text']='''
item,price,category
A,10,low
A,15,high
A,100,
B,10,low
B,35,high
B,100,
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``price`` を範囲で
分類項目 ``low、middle、high`` を結合する。
'''
script['sh_code']='''
mrjoin r=price%n m=ref1.csv R=range f=category i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mrjoin(rf="price%n", m="ref1.csv", R="range", f="category", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='基本例2'
script['comment']='''
'''
script['sh_code']='''
mrjoin -lo r=price%n m=ref1.csv R=range f=category i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mrjoin(lo=True, rf="price%n", m="ref1.csv", R="range", f="category", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='基本例3'
script['comment']='''
'''
script['sh_code']='''
mrjoin -n r=price%n m=ref1.csv R=range f=category i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mrjoin(n=True, rf="price%n", m="ref1.csv", R="range", f="category", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='商品別に異なる範囲を設定して結合'
script['comment']='''
'''
script['sh_code']='''
mrjoin k=item r=price%n m=ref2.csv f=category i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.mrjoin(k="item", rf="price%n", m="ref2.csv", f="category", i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

