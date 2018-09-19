# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mtonull'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
item,quantity,price
A,0,1
B,1,0
C,2,200
D,3,0
E,0,298
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
item,price
fruit:apple,100
fruit:peach,250
fruit:grape,300
fruit:pineapple,450
fruit:orange,500
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``quantity`` と ``price`` 項目が0をNULL値に置換する。
'''
script['sh_code']='''
mtonull f=quantity,price v=0 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mtonull(f="quantity,price", v="0", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='NULL値に置換する数字の指定'
script['comment']='''
``quantity`` と ``price`` 項目が0もしくは1をNULL値に置換する。
'''
script['sh_code']='''
mtonull f=quantity,price v=0,1 i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mtonull(f="quantity,price", v="0,1", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='部分文字列マッチでの置換'
script['comment']='''
``quantity`` と ``price`` 項目が0を含めばNULL値に置換する。
'''
script['sh_code']='''
mtonull -sub f=quantity,price v=0 i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mtonull(sub=True, f="quantity,price", v="0", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='指定の文字列の置換'
script['comment']='''
``item`` 項目に ``apple、orange、pineapple`` を含む値をNULL値に置換する。
'''
script['sh_code']='''
mtonull f=item v=apple,orange,pineapple -sub i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.mtonull(f="item", v="apple,orange,pineapple", sub=True, i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

