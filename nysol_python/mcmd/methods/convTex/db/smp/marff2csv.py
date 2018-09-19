# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='marff2csv'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.arff'
data['text']='''
@RELATION       customerPurchaseData
@ATTRIBUTE      customer    string
@ATTRIBUTE      date    date yyyyMMdd
@ATTRIBUTE      quantity    numeric
@ATTRIBUTE      amount    numeric
@ATTRIBUTE      item    {A,B}
@DATA
No.1,20081201,1,10,A
No.2,20081202,2,20,A
No.3,20081203,3,30,A
No.4,20081201,4,40,B
No.5,20081203,5,50,B
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
arff形式の顧客購買データをcsv形式のデータへ変換する。
'''
script['sh_code']='''
marff2csv i=dat1.arff  o=rsl1.csv
'''
script['py_code']='''
nm.marff2csv(i="dat1.arff", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

