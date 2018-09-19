# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mcombi'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,item
A,a1
A,a2
A,a3
B,a4
B,a5
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``customer`` 項目を単位に、 ``item`` 項目の2アイテムの組み合わせを求め、
``item1,item2`` という項目名で出力する。
``k=,f=`` で指定していない項目(ここでは ``item`` 項目)は、キーの最終行の値が出力される。
'''
script['sh_code']='''
mcombi k=customer f=item n=2 a=item1,item2 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcombi(k="customer", f="item", n="2", a="item1,item2", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='基本例2'
script['comment']='''
``dup=True`` オプションを指定すると同一のアイテムの組み合せも出力される。
'''
script['sh_code']='''
mcombi k=customer f=item n=2 a=item1,item2 i=dat1.csv o=rsl2.csv -dup
'''
script['py_code']='''
nm.mcombi(k="customer", f="item", n="2", a="item1,item2", i="dat1.csv", o="rsl2.csv", dup=True).run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='順列を求める例'
script['comment']='''
``customer`` 項目を単位に、 ``item`` 項目の2アイテムの順列を求め、
``item1,item2`` という項目名で出力する。
'''
script['sh_code']='''
mcombi k=customer f=item n=2 a=item1,item2 -p i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcombi(k="customer", f="item", n="2", a="item1,item2", p=True, i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='順列を求める例'
script['comment']='''
``item`` 項目を降順に並べ替えた後、
``item`` 項目の2アイテムの順列を求める。
'''
script['sh_code']='''
mcombi k=customer f=item n=2 s=item%r a=item1,item2 -p i=dat1.csv o=rsl4.csv
'''
script['py_code']='''
nm.mcombi(k="customer", f="item", n="2", s="item%r", a="item1,item2", p=True, i="dat1.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

