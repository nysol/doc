# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mselrand'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,date,amount
A,20081201,10
A,20081207,20
A,20081213,30
B,20081002,40
B,20081209,50
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
C,20081210,60
D,20081201,70
D,20081205,80
D,20081209,90
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
一人の顧客につきランダムに1行を選択する。
'''
script['sh_code']='''
mselrand k=顧客 c=1 S=1 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mselrand(k="customer", c="1", S="1", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='ランダムに一定割合の行を選択'
script['comment']='''
一人の顧客につきランダムに50\%の行を選択する。
また、それ以外の不一致データは ``oth2.csvと`` いうファイルに出力する。
'''
script['sh_code']='''
mselrand k=顧客 p=50 S=1 u=oth2.csv i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mselrand(k="customer", p="50", S="1", u="oth2.csv", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='oth2.csv,rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='キー単位の選択'
script['comment']='''
以下の例は、顧客 ``A,B,C,D`` の4人からランダムに2人を選ぶ。
顧客 ``D`` が選ばれると、顧客 ``D`` の行は全て出力される。
'''
script['sh_code']='''
mselrand k=顧客 c=2 S=1 -B i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mselrand(k="customer", c="2", S="1", B=True, i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

