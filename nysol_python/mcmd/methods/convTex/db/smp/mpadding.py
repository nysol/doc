# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mpadding'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
no
3
6
8
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
date,dummy
20130929,a
20131002,b
20131004,c
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``no`` 項目が整数(\%n)として連続するようにレコードをパディングする。
``1`` とverb|4|の間に ``2,3`` を、 ``4`` と ``2`` の間に ``3`` が挿入されている。
'''
script['sh_code']='''
mpadding f=no%n i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mpadding(f="no%n", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='開始値、終了値の指定'
script['comment']='''
行間のパディングだけでなく、先頭行/終端行の前後もパディングする。
前後の範囲は ``S=,E=`` で指定する。
'''
script['sh_code']='''
mpadding f=no%n S=1 E=10 i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mpadding(f="no%n", S="1", E="10", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='日付パディング'
script['comment']='''
``date`` 項目が日付(\%d)として連続するようにレコードをパディングする。
``k=,f=`` で指定した以外の項目は、直前の行の項目値でパディングする。
'''
script['sh_code']='''
mpadding f=date%d i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mpadding(f="date%d", i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='パディング用文字列指定'
script['comment']='''
``v=`` にてパディング文字列を指定することもできる。
'''
script['sh_code']='''
mpadding f=date%d v=padding i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.mpadding(f="date%d", v="padding", i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='パディングにNULL値を指定'
script['comment']='''
``n=True`` を指定してNULL値でパディングすることも可能。
'''
script['sh_code']='''
mpadding f=date%d -n i=dat2.csv o=rsl5.csv
'''
script['py_code']='''
nm.mpadding(f="date%d", n=True, i="dat2.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

