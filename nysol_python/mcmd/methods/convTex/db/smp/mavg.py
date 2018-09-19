# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mavg'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,quantity,amount
A,1,5
A,2,20
B,1,15
B,,10
B,5,20
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``customer`` 項目を単位に ``quantity`` と ``amount`` 項目の平均値を計算し、 ``qttTotal`` と ``amtTotal`` という項目名で出力する。
'''
script['sh_code']='''
mavg k=顧客 f=数量:数量平均,金額:金額平均 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mavg(k="customer", f="quantity:qttTotal,amount:amtTotal", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='NULL値がある場合の出力'
script['comment']='''
``customer`` 項目を単位に ``quantity`` と ``amount`` 項目の平均値を計算し、 ``qttTotal`` と ``amtTotal`` という項目名で出力する。
``n=True`` オプションを指定することで、NULL値が含まれている場合は、結果もNULL値として出力する。
'''
script['sh_code']='''
mavg k=顧客 f=数量:数量平均,金額:金額平均 -n i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mavg(k="customer", f="quantity:qttTotal,amount:amtTotal", n=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='顧客項目を単位としない例'
script['comment']='''
``quantity`` と ``amount`` 項目の平均値を計算し、 ``qttTotal`` と ``amtTotal`` という項目名で出力する。
'''
script['sh_code']='''
mavg f=数量:数量平均,金額:金額平均 i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mavg(f="quantity:qttTotal,amount:amtTotal", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

