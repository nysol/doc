# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='msim'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
x,y,z
14,0.17,-14
11,0.2,-1
32,0.15,-2
13,0.33,-2
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
key,x,y,z
A,14,0.17,-14
A,11,0.2,-1
A,32,0.15,-2
B,13,0.33,-2
B,10,0.8,-5
B,15,0.45,-9
'''
db['idatas'].append(data)

data={}
data['name']='dat3.csv'
data['text']='''
x,y,z
1,1,0
1,0,1
1,0,1
0,1,1
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``x、y、z`` 項目の2項目間の組み合わせについて
ピアソンの積率相関係数とコサインを計算する。
'''
script['sh_code']='''
msim c=pearson,cosine f=x,y,z i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.msim(c="pearson,cosine", f="x,y,z", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='対角行列、上三角行列を出力'
script['comment']='''
``x、y、z`` 項目の2項目間の組み合わせについて
ピアソンの積率相関係数とコサインを計算する。(dオプションあり)
'''
script['sh_code']='''
msim c=pearson,cosine f=x,y,z -d i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.msim(c="pearson,cosine", f="x,y,z", d=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='キー単位での計算'
script['comment']='''
``key`` 項目を単位にして計算する。
'''
script['sh_code']='''
msim k=key c=pearson,cosine f=x,y,z i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.msim(k="key", c="pearson,cosine", f="x,y,z", i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='類似度名の指定'
script['comment']='''
01値のデータに付いての計算。ハミング距離とphi係数を計算する。
'''
script['sh_code']='''
msim c=hamming,phi f=x,y,z i=dat3.csv o=rsl4.csv
'''
script['py_code']='''
nm.msim(c="hamming,phi", f="x,y,z", i="dat3.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='類似度名の変更'
script['comment']='''
01値のデータに付いての計算。ハミング距離とphi係数を計算し、
出力項目名を変更する。
'''
script['sh_code']='''
msim c=hamming:ハミング距離,phi:ファイ係数 a=変数1,変数2 f=x,y,z i=dat3.csv o=rsl5.csv
'''
script['py_code']='''
nm.msim(c="hamming:ハミング距離,phi:ファイ係数", a="変数1,変数2", f="x,y,z", i="dat3.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

