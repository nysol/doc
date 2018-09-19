# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='msel'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,quantity,amount
A,1,10
A,2,20
B,1,30
B,3,40
B,1,50
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
a,b
A,-1
B,
C,1
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``amount`` 項目の値が40より大きい行を選択する。
それ以外のデータは ``unmatch1.csv`` に出力する。
'''
script['sh_code']='''
msel c='${金額}>40' u=unmatch1.csv i=dat1.csv o=match1.csv
'''
script['py_code']='''
nm.msel(c="${amount}>40", u="unmatch1.csv", i="dat1.csv", o="match1.csv").run()
'''
script['odatas']='unmatch1.csv,match1.csv'
db['scripts'].append(script)

script={}
script['title']='NULL値の選択規制'
script['comment']='''
``msel`` コマンドでは ``c=`` で与えられた式を評価した結果がNULL値の場合その行は選択されない。
また、アンマッチ出力ファイルが ``u=`` によって指定されていれば、そのファイルに出力される。
以下の例では項目 ``b`` に ``1=True`` 、NULL値、 ``1`` を持つ3行のデータについて、0より大きい行を選択しているが、
NULL値を含む行はアンマッチ出力ファイルへと出力される。
'''
script['sh_code']='''
msel c='${b}>0' i=dat2.csv o=match2.csv u=unmatch2.csv
'''
script['py_code']='''
nm.msel(c="${b}>0", i="dat2.csv", o="match2.csv", u="unmatch2.csv").run()
'''
script['odatas']='match2.csv,unmatch2.csv'
db['scripts'].append(script)

script={}
script['title']='-rオプション指定'
script['comment']='''
真偽は逆転するがNULL値の評価に変わりはない。
すなわちNULL値の行は選択されない。
以下の例では、上の例と同様のデータおよび選択条件で ``r=True`` をつけている。
真偽の選択条件は逆転しているが、NULL値を含む行は上記の例と同様にアンマッチファイルへと出力されていることがわかる。
'''
script['sh_code']='''
msel -r c='${b}>0' i=dat2.csv o=match3.csv u=unmatch3.csv
'''
script['py_code']='''
nm.msel(r=True, c="${b}>0", i="dat2.csv", o="match3.csv", u="unmatch3.csv").run()
'''
script['odatas']='match3.csv,unmatch3.csv'
db['scripts'].append(script)

