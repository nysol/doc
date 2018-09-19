# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mfldname'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,itemID,10月
a,xx,11
b,yy,122
c,zz,
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
a,xx,11
b,yy,122
c,zz,
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
項目名の ``customer`` を「cust」に、「10月」を「Oct.」に変更する。
'''
script['sh_code']='''
mfldname f=顧客:cust,10月:Oct. i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mfldname(f="customer:cust,10月:Oct.", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='項目名変更'
script['comment']='''
項目名を ``x,y,z`` に変更する。
'''
script['sh_code']='''
mfldname n=x,y,z i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mfldname(n="x,y,z", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='項目名行がないデータ'
script['comment']='''
'''
script['sh_code']='''
mfldname -nfni n=x,y,z i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mfldname(nfni=True, n="x,y,z", i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

