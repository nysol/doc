# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mmvavg'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,value
1,5
2,1
3,3
4,4
5,4
6,6
7,1
8,4
9,7
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,key,value
1,a,5
2,a,1
3,a,3
4,a,4
5,a,4
6,b,6
7,b,1
8,b,4
9,b,7
'''
db['idatas'].append(data)

data={}
data['name']='dat3.csv'
data['text']='''
key,value
a,1
a,2
a,3
a,4
a,5
b,6
b,1
b,4
b,7
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
最初の行は期数に満たないため出力されない。
'''
script['sh_code']='''
mmvavg s=id f=value t=2 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mmvavg(s="id", f="value", t="2", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='基本例2'
script['comment']='''
最初の行は期数に満たないため出力されない。
'''
script['sh_code']='''
mmvavg s=id f=value t=2 -w i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mmvavg(s="id", f="value", t="2", w=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='基本例3'
script['comment']='''
指数平滑移動平均( ``exp=True`` )の場合は最初の行から出力される。
'''
script['sh_code']='''
mmvavg s=id f=value t=2 -exp i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mmvavg(s="id", f="value", t="2", exp=True, i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='キーを指定する例'
script['comment']='''
'''
script['sh_code']='''
mmvavg s=key,id k=key f=value t=2 i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.mmvavg(s="key,id", k="key", f="value", t="2", i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='指定した期に満たなくても出力する例'
script['comment']='''
'''
script['sh_code']='''
mmvavg -q k=key f=value t=2 skip=0 i=dat3.csv o=rsl5.csv
'''
script['py_code']='''
nm.mmvavg(q=True, k="key", f="value", t="2", skip="0", i="dat3.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

