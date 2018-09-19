# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mnrcommon'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
date,amount
20080123,10
20080203,10
20080203,20
20080203,45
200804l0,50
'''
db['idatas'].append(data)

data={}
data['name']='ref1.csv'
data['text']='''
date,amountF,amountT
20080203,5,15
20080203,40,50
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
日付項目の値が ``20080203`` で、 ``amount`` 項目の値が ``5`` 以上 ``15`` 未満の行、および ``40`` 以上 ``50`` 未満の行を選択する。
'''
script['sh_code']='''
mnrcommon k=日付 m=ref1.csv R=金額F,金額T r=金額%n i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mnrcommon(k="date", m="ref1.csv", R="amountF,amountT", rf="amount%n", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='条件反転'
script['comment']='''
``r=True`` を付けると選択条件は反転する。
'''
script['sh_code']='''
mnrcommon k=日付 m=ref1.csv R=金額F,金額T r=金額%n -r i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mnrcommon(k="date", m="ref1.csv", R="amountF,amountT", rf="amount%n", r=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

