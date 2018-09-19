# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mnumber'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
Customer,Val,Sum
A,29,300
B,35,250
C,15,200
D,23,150
E,10,100
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
Date
20090101
20090101
20090102
20090103
20090103
'''
db['idatas'].append(data)

data={}
data['name']='dat3.csv'
data['text']='''
Customer,Val,Sum
A,3,300
B,1,250
C,2,250
D,1,150
E,1,100
'''
db['idatas'].append(data)

data={}
data['name']='dat4.csv'
data['text']='''
Customer,Val,Sum
A,1,100
B,1,150
C,1,250
D,2,250
E,3,300
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='数字の連番'
script['comment']='''
Customer項目名順（昇順）に連番を振り「No」という項目名で出力する。
'''
script['sh_code']='''
mnumber s=Customer a=No i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mnumber(s="Customer", a="No", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='Date項目順の連番'
script['comment']='''
Date項目順（昇順）に連番をふる。その際、同じDateには同じNoを振り「No」という項目名で出力する。
'''
script['sh_code']='''
mnumber k=Date a=No -B i=dat2.csv o=rsl2.csv
'''
script['py_code']='''
nm.mnumber(k="Date", a="No", B=True, i="dat2.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='Sum項目順の連番(同Rankは同じアルファベットをふる)'
script['comment']='''
Sum項目の多い順（降順）にアルファベットのAから順に連文字を振り「Rank」という項目名で出力する。
また、同Rankの場合は同じアルファベット文字を振ることにする。
'''
script['sh_code']='''
mnumber a=Rank e=same s=Sum%nr S=A  i=dat3.csv o=rsl3.csv
'''
script['py_code']='''
nm.mnumber(a="Rank", e="same", s="Sum%nr", S="A", i="dat3.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='Sum項目順の連番(同Rankは並び順でNoをふる)'
script['comment']='''
Sum項目の多い順（降順）に連番を振り「Rank」という項目名で出力する。
その際、同Rankの場合は並び順でNoを振ることにする。
'''
script['sh_code']='''
mnumber a=Rank e=seq s=Sum%nr i=dat3.csv o=rsl4.csv
'''
script['py_code']='''
nm.mnumber(a="Rank", e="seq", s="Sum%nr", i="dat3.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='Sum項目順の連番(同Rankは同じNoをふる)'
script['comment']='''
Sum項目の多い順（降順）に連番を振り「Rank」という項目名で出力する。
その際、同Rankの場合は同じNoを振ることにする。
'''
script['sh_code']='''
mnumber a=Rank e=same s=Sum%nr i=dat3.csv o=rsl5.csv
'''
script['py_code']='''
nm.mnumber(a="Rank", e="same", s="Sum%nr", i="dat3.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

script={}
script['title']='Sum項目順の連番(同Rankの場合は同じRankNoを振り、次のNoはスキップ)'
script['comment']='''
Sum項目の多い順（降順）に連番を振り「Rank」という項目名で出力する。
その際、同Rankの場合は同じRankNoを振り、次のNoはスキップするようにNoを振ることにする。
'''
script['sh_code']='''
mnumber a=Rank e=skip s=Sum%nr i=dat3.csv o=rsl6.csv
'''
script['py_code']='''
nm.mnumber(a="Rank", e="skip", s="Sum%nr", i="dat3.csv", o="rsl6.csv").run()
'''
script['odatas']='rsl6.csv'
db['scripts'].append(script)

script={}
script['title']='10から始まる連番'
script['comment']='''
Sum項目の小さい順（昇順）に10から始まる連番を振り「Score」という項目名で出力する。
その際、同Rankの場合は同じRankNoを振り、次のNoはスキップするようにNoを振ることにする。
'''
script['sh_code']='''
mnumber a=Score e=same s=Sum%n S=10 i=dat4.csv o=rsl7.csv
'''
script['py_code']='''
nm.mnumber(a="Score", e="same", s="Sum%n", S="10", i="dat4.csv", o="rsl7.csv").run()
'''
script['odatas']='rsl7.csv'
db['scripts'].append(script)

script={}
script['title']='10から始まる5つ飛びの連番'
script['comment']='''
Sum項目の小さい順番（昇順）に10から始まる5つ飛びの連番を振り「Score」という項目名で出力する。
また、同Rankの場合は同じNoを振ることにする。
'''
script['sh_code']='''
mnumber a=Score e=same s=Sum%n S=10 I=5 i=dat4.csv o=rsl8.csv
'''
script['py_code']='''
nm.mnumber(a="Score", e="same", s="Sum%n", S="10", I="5", i="dat4.csv", o="rsl8.csv").run()
'''
script['odatas']='rsl8.csv'
db['scripts'].append(script)

