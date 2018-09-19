# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='msed'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,zipCode
A,6230041
B,6240053
C,6330032
D,6230087
E,6530095
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
item,price
fruit:apple,100
fruit:peach,250
fruit:pineapple,300
fruit:orange,450
fruit:grapefruit,500
'''
db['idatas'].append(data)

data={}
data['name']='dat3.csv'
data['text']='''
str1
abc
abbc
ac
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``zipCode`` 項目の値が00から始まる4桁文字列を ``####`` に置換する。
'''
script['sh_code']='''
msed f=zipCode c=00.. v=#### i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.msed(f="zipCode", c="00..", v="####", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='項目名指定'
script['comment']='''
``zipCode`` の値が00から始まる4桁の数字を ``####`` に置換し、 ``zipCode4`` という項目名で出力する。
'''
script['sh_code']='''
msed f=zipCode:zipCode4 c='00\d\d' v=#### i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.msed(f="zipCode:zipCode4", c="00\d\d", v="####", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='グローバル置換'
script['comment']='''
``zipCode`` の値が ``0`` を全て ``=True`` にグローバル置換する。
'''
script['sh_code']='''
msed f=zipCode c=0 v=- -g i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.msed(f="zipCode", c="0", v="-", g=True, i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='部分置換'
script['comment']='''
``item`` の先頭の ``fruit`` を削除する。
先頭一致( ``^`` )を指定しているので、最後の行の ``grapefruit`` は削除されていないことに注意する。
'''
script['sh_code']='''
msed f=item c='^fruit' v= -g i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.msed(f="item", c="^fruit", v="", g=True, i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='マッチ結果を用いた置換'
script['comment']='''
``v=`` の中で ``$&`` を用いれば、マッチした文字列(連続した ``b`` )に置き換わる。
'''
script['sh_code']='''
msed f=str1 c='b+' v='#$&#' i=dat3.csv o=rsl5.csv
'''
script['py_code']='''
nm.msed(f="str1", c="b+", v="#$&#", i="dat3.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

script={}
script['title']='グローバルマッチとの組み合せ'
script['comment']='''
グローバルマッチにすると、個々のマッチ毎に ``v=`` の内容が評価される。
'''
script['sh_code']='''
msed f=str1 c=b v='#$&#' -g i=dat3.csv o=rsl6.csv
'''
script['py_code']='''
nm.msed(f="str1", c="b", v="#$&#", g=True, i="dat3.csv", o="rsl6.csv").run()
'''
script['odatas']='rsl6.csv'
db['scripts'].append(script)

script={}
script['title']='プレフィックス置換'
script['comment']='''
``$``` にて、マッチした箇所の前の文字列(プレフィックス)に置換される。
'''
script['sh_code']='''
msed f=str1 c=b v='#$`#' i=dat3.csv o=rsl7.csv
'''
script['py_code']='''
nm.msed(f="str1", c="b", v="#$`#", i="dat3.csv", o="rsl7.csv").run()
'''
script['odatas']='rsl7.csv'
db['scripts'].append(script)

script={}
script['title']='サフィックス置換'
script['comment']='''
``$'`` にて、マッチした箇所の後の文字列(サフィックス)に置換される。
'''
script['sh_code']='''
msed f=str1 c=b v="#$'#" i=dat3.csv o=rsl8.csv
'''
script['py_code']='''
nm.msed(f="str1", c="b", v="#$'#", i="dat3.csv", o="rsl8.csv").run()
'''
script['odatas']='rsl8.csv'
db['scripts'].append(script)

