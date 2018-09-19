# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mbest'

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
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
この例では、 ``quantity`` と ``amount`` 項目値の大きい順（降順）に並べ替えている。
``from=`` , ``to=`` , ``size=`` を指定しなければ先頭行(0行目)のみ選択する
'''
script['sh_code']='''
mbest s=数量%nr,金額%nr i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mbest(s="quantity%nr,amount%nr", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='基本例2'
script['comment']='''
``customer`` で並べ替えた後、先頭行(0行目)から3行選択する
'''
script['sh_code']='''
mbest s=顧客 from=0 size=3 i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mbest(s="customer", fr="0", size="3", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='基本例3'
script['comment']='''
並べ替えを行わず(もとのレコード順序を維持したまま)、0行目から1行目まで選択する
'''
script['sh_code']='''
mbest -q from=0 to=1 i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mbest(q=True, fr="0", to="1", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='条件反転'
script['comment']='''
顧客の初回来店日以外の行を選択する。
初回来店日は ``fvd.csv`` というファイルに出力する。
'''
script['sh_code']='''
mbest s=顧客,日付 k=顧客 -r u=fvd.csv i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.mbest(s="customer,date", k="customer", r=True, u="fvd.csv", i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='fvd.csv,rsl4.csv'
db['scripts'].append(script)

