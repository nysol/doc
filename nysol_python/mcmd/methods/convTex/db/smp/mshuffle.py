# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mshuffle'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,quantity,amount
A,20,5200
B,18,4000
C,15,3500
D,10,2000
E,3,800
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
customer,date,amount
A,20081201,10
A,20081207,20
A,20081213,30
B,20081002,40
B,20081209,50
C,20081003,60
C,20081219,20
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
指定した項目の値(顧客)が同じであれば同一のファイルに出力にされるように2つのファイルに分割する
'''
script['sh_code']='''
mshuffle f=顧客 d=./dat/d n=2 i=dat2.csv
'''
script['py_code']='''
nm.mshuffle(f="customer", d="./dat/d", n="2", i="dat2.csv").run()
'''
script['odatas']=''
db['scripts'].append(script)

script={}
script['title']='f=を指定しない例'
script['comment']='''
f=を指定せず2つのファイルに分割する。
行番号のhash値を用いるので、2つのファイルの行数はほぼ等しくなる。
'''
script['sh_code']='''
mshuffle d=./dat/d n=2 i=dat2.csv
'''
script['py_code']='''
nm.mshuffle(d="./dat/d", n="2", i="dat2.csv").run()
'''
script['odatas']=''
db['scripts'].append(script)

script={}
script['title']='v=,f=の指定'
script['comment']='''
v=2,1を指定することで、ファイル0(d\_0)には2つのhash値を割り当て、
ファイル1(d\_1)には1つのhash値を割り当てて分割する。
'''
script['sh_code']='''
mshuffle f=顧客 d=./dat/d v=2,1 i=dat2.csv
'''
script['py_code']='''
nm.mshuffle(f="customer", d="./dat/d", v="2,1", i="dat2.csv").run()
'''
script['odatas']=''
db['scripts'].append(script)

script={}
script['title']='v=の指定'
script['comment']='''
例3をf=の指定なしで実行する。
行番号のhash値を用いるので、この場合は出力行数の比と重みの比がほぼ等しくなる。
'''
script['sh_code']='''
mshuffle d=./dat/d v=2,1 i=dat2.csv
'''
script['py_code']='''
nm.mshuffle(d="./dat/d", v="2,1", i="dat2.csv").run()
'''
script['odatas']=''
db['scripts'].append(script)

