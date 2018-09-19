# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mcommon'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,quantity
A,1
B,2
C,1
D,3
E,1
'''
db['idatas'].append(data)

data={}
data['name']='ref1.csv'
data['text']='''
customer,gender
A,female
B,male
E,female
'''
db['idatas'].append(data)

data={}
data['name']='ref2.csv'
data['text']='''
customerID,gender
A,female
B,male
E,female
'''
db['idatas'].append(data)

data={}
data['name']='dat3.csv'
data['text']='''
customer,quantity
A,1
A,2
A,3
B,1
D,1
D,2
'''
db['idatas'].append(data)

data={}
data['name']='ref3.csv'
data['text']='''
customer
A
A
D
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
入力ファイルにある ``customer`` 項目と、参照ファイルにある ``customer`` 項目が同じ値を持つ入力ファイルの行を選択する。
それ以外のデータは ``oth.csv`` に出力する。
'''
script['sh_code']='''
mcommon k=顧客 m=ref1.csv u=oth.csv i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcommon(k="customer", m="ref1.csv", u="oth.csv", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='oth.csv,rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='同じ値を持たない入力ファイルの行選択'
script['comment']='''
``r=True`` オプションを付けることで、条件が逆転し、参照ファイルにない ``customer`` を選択することになる。
'''
script['sh_code']='''
mcommon k=顧客 m=ref1.csv -r i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcommon(k="customer", m="ref1.csv", r=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='結合キー項目名が異なる場合'
script['comment']='''
結合キーの項目名が異なる場合は、 ``K=`` で指定する。
'''
script['sh_code']='''
mcommon k=顧客 K=顧客ID i=dat1.csv m=ref2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcommon(k="customer", K="customerID", i="dat1.csv", m="ref2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='キー項目に重複行がある場合の例'
script['comment']='''
参照ファイルと入力ファイルのキー項目に重複行があっても選択可能。
'''
script['sh_code']='''
mcommon k=顧客 m=ref3.csv -r i=dat3.csv o=rsl4.csv
'''
script['py_code']='''
nm.mcommon(k="customer", m="ref3.csv", r=True, i="dat3.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

