# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mnrjoin'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
date,price
20080123,10
20080123,20
20080203,10
20080203,35
200804l0,50
'''
db['idatas'].append(data)

data={}
data['name']='ref1.csv'
data['text']='''
date,priceF,priceT,avg
20080203,5,15,150
20080203,40,50,200
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
日付項目の値が ``20080203`` で、 ``amount`` 項目の値が ``5`` 以上 ``15`` 未満の入力データ行には ``avg=150`` を、
``40`` 以上 ``50`` 未満の行には ``avg=200`` を結合する。
'''
script['sh_code']='''
mnrjoin k=date f=avg m=ref1.csv R=priceF,priceT r=price%n i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mnrjoin(k="date", f="avg", m="ref1.csv", R="priceF,priceT", rf="price%n", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='未結合データ出力'
script['comment']='''
``n=True`` を指定することで、参照ファイルにマッチしない入力ファイルの行( ``avg=`` がNULL値の行)も出力し、
``N=True`` を指定することで、入力ファイルにマッチしない参照ファイルの行( ``price=`` がNULL値の行)も出力する。
いわゆる外部結合である。
'''
script['sh_code']='''
mnrjoin k=date f=avg m=ref1.csv R=priceF,priceT r=price%n -n -N i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mnrjoin(k="date", f="avg", m="ref1.csv", R="priceF,priceT", rf="price%n", n=True, N=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

