# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mnullto'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,birthday
A,19690103
B,
C,19500501
D,
E,
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,date
A,19690103
B,
C,19500501
D,
E,
'''
db['idatas'].append(data)

data={}
data['name']='dat3.csv'
data['text']='''
id,seq,val
A,1,1
A,3,2
A,2,
B,2,3
B,1,
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``birthday`` 項目がNULL値の場合は ``"no value"`` に置換する。
'''
script['sh_code']='''
mnullto f=birthday v="no value" i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mnullto(f="birthday", v="no value", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='NULL値以外の置換'
script['comment']='''
``birthday`` 項目がNULL値の場合は、 ``"no value"``
値がある場合は ``"value"`` 置換し ``entry`` という項目名に変更して出力する。
'''
script['sh_code']='''
mnullto f=birthday:entry v="no value" O="value" i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mnullto(f="birthday:entry", v="no value", O="value", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='新しい項目を出力'
script['comment']='''
``birthday`` 項目がNULL値の場合は ``"no value"`` 、値がある場合は ``"value"`` に置換し ``entry`` という項目名で出力する。
'''
script['sh_code']='''
mnullto f=birthday:entry v="no value" O="value" -A i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mnullto(f="birthday:entry", v="no value", O="value", A=True, i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='前行の値に置換'
script['comment']='''
'''
script['sh_code']='''
mnullto f=val -p i=dat3.csv o=rsl4.csv
'''
script['py_code']='''
nm.mnullto(f="val", p=True, i="dat3.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='キー項目を指定した場合の例'
script['comment']='''
'''
script['sh_code']='''
mnullto k=id s=seq f=val -p i=dat3.csv o=rsl5.csv
'''
script['py_code']='''
nm.mnullto(k="id", s="seq", f="val", p=True, i="dat3.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

