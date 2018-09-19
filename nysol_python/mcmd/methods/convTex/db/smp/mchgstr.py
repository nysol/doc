# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mchgstr'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,item
1,01
2,02
3,03
4,04
5,05
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,item
1,0111
2,0121
3,0231
4,0241
5,0151
'''
db['idatas'].append(data)

data={}
data['name']='dat3.csv'
data['text']='''
id,city
1,奈良市
2,下市町
3,十津川村
4,五條市
5,山添村
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``item`` の値が
``"01"`` を ``"A"`` に、
``"03"`` を ``"B"`` に、
``"04"`` を ``"C"`` に置換する。
その他はNULL値として出力する。
'''
script['sh_code']='''
mchgstr f=item c=01:A,03:B,05:C i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mchgstr(f="item", c="01:A,03:B,05:C", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='条件に合致しない値を置換する文字列の指定'
script['comment']='''
``O=`` パラメータを指定することで、
置換条件に合致しない場合は ``"out of range"`` という文字列に置換して出力する。
'''
script['sh_code']='''
mchgstr f=item c=01:A,03:B,05:C O="out of range" i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mchgstr(f="item", c="01:A,03:B,05:C", O="out of range", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='新しい項目として出力'
script['comment']='''
``A=True`` オプションを付けることで、新しい項目( ``item info`` )として出力する。
'''
script['sh_code']='''
mchgstr f=item:"item info" c=01:A,03:B,05:C O="out of range" -A i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mchgstr(f="item:item info", c="01:A,03:B,05:C", O="out of range", A=True, i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='条件外を項目の値として出力'
script['comment']='''
``F=True`` オプションを付けることで、
置換条件に合致しない場合は、元の値をそのまま出力する。
'''
script['sh_code']='''
mchgstr f=item c=01:A,03:B,05:C -F i=dat1.csv o=rsl4.csv
'''
script['py_code']='''
nm.mchgstr(f="item", c="01:A,03:B,05:C", F=True, i="dat1.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='条件を部分文字列マッチで置換'
script['comment']='''
``sub=True`` オプションをつけることで、部分文字列の置換となる。
以下の例では、 ``item`` 項目に文字列 ``"01"`` が含まれていれば、それを ``"A"`` に置換する。
'''
script['sh_code']='''
mchgstr f=item c=01:A -sub i=dat2.csv o=rsl5.csv
'''
script['py_code']='''
nm.mchgstr(f="item", c="01:A", sub=True, i="dat2.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

script={}
script['title']='ワイド文字での部分文字列マッチ'
script['comment']='''
ワイド文字の部分文字列置換をする場合は ``W=True`` オプションを用いる。
ただし、UTF-8エンコーディングを用いているのであれば ``W=True`` をつけなくても正しく動作する。
詳しくは「\hyperref[sect:multibyte]{マルチバイト文字}」の節を参照されたい。
'''
script['sh_code']='''
mchgstr f=city c=市:01,町:02,村:02 -sub -W i=dat3.csv o=rsl6.csv
'''
script['py_code']='''
nm.mchgstr(f="city", c="市:01,町:02,村:02", sub=True, W=True, i="dat3.csv", o="rsl6.csv").run()
'''
script['odatas']='rsl6.csv'
db['scripts'].append(script)

