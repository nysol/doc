# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='msplit'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,data
A,1 10 2
A,2 20 3
B,1 15 5
B,3 10 4
B,1 20 6
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,data
A,1 10 2
A,2 20 3
B,1 15 5
B,3 4
B,1
'''
db['idatas'].append(data)

data={}
data['name']='dat3.csv'
data['text']='''
id,data
A,1_10_3
A,2_20_5
B,1_15_6
B,3_10_7
B,1_20_8
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
半角スペースで分割
'''
script['sh_code']='''
msplit f=data a=d1,d2,d3 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.msplit(f="data", a="d1,d2,d3", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='-r利用'
script['comment']='''
``r=True`` を指定することで、 ``f=`` で項目を削除できる。
'''
script['sh_code']='''
msplit f=data a=d1,d2,d3 -r i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.msplit(f="data", a="d1,d2,d3", r=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='分割数不一致'
script['comment']='''
``a=`` で指定した項目数よりも分割できる項目数が少ない場合は、NULLが追加され、
多い場合、先頭から指定した分割数まで出力する
'''
script['sh_code']='''
msplit f=data a=d1,d2 i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.msplit(f="data", a="d1,d2", i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='delim指定'
script['comment']='''
``delim=`` を使用して半角スペース以外の文字で分割する
'''
script['sh_code']='''
msplit f=data a=d1,d2,d3 delim=_ i=dat3.csv o=rsl4.csv
'''
script['py_code']='''
nm.msplit(f="data", a="d1,d2,d3", delim="_", i="dat3.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

