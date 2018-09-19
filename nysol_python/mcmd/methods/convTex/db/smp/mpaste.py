# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mpaste'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id1
1
2
3
4
'''
db['idatas'].append(data)

data={}
data['name']='ref1.csv'
data['text']='''
id2
a
b
c
d
'''
db['idatas'].append(data)

data={}
data['name']='ref2.csv'
data['text']='''
id2
a
b
'''
db['idatas'].append(data)

data={}
data['name']='ref3.csv'
data['text']='''
id2,val
a,R0
b,R1
c,R2
d,R3
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mpaste m=ref1.csv i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mpaste(m="ref1.csv", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='行数が異なる例'
script['comment']='''
入力ファイルと参照ファイルで行数が異なる場合は、少いファイルの行数に合わせる。
'''
script['sh_code']='''
mpaste m=ref2.csv i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mpaste(m="ref2.csv", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='外部結合'
script['comment']='''
``n=True`` を指定すると、参照ファイルの行数が少なくても、対応しない入力ファイルの行もNULL値を結合して出力する。
'''
script['sh_code']='''
mpaste m=ref2.csv -n i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mpaste(m="ref2.csv", n=True, i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='結合項目を指定'
script['comment']='''
'''
script['sh_code']='''
mpaste f=val m=ref3.csv i=dat1.csv o=rsl4.csv
'''
script['py_code']='''
nm.mpaste(f="val", m="ref3.csv", i="dat1.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

