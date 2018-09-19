# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mrand'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer
A
B
C
D
E
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
customer
A
A
A
B
B
C
D
D
D
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
0.0から1.0の範囲の実数乱数を生成する。
'''
script['sh_code']='''
mrand a=rand i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mrand(a="rand", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='基本例2'
script['comment']='''
-intで整数乱数
'''
script['sh_code']='''
mrand a=rand -int i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mrand(a="rand", int=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='最小値、最大値を決めた乱数の生成'
script['comment']='''
最小値が10、最大値が100の整数の乱数を生成し、 ``rand`` という項目名で出力する。
'''
script['sh_code']='''
mrand a=rand -int min=10 max=100 S=1 i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mrand(a="rand", int=True, min="10", max="100", S="1", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='キー単位の乱数生成'
script['comment']='''
以下の例は、顧客 ``A,B,C,D`` の4人について同じ顧客には同じ乱数値を振る。
'''
script['sh_code']='''
mrand k=顧客 -int min=0 max=1 a=rand i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.mrand(k="customer", int=True, min="0", max="1", a="rand", i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

