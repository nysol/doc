# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mvcommon'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
items1,items2
b a c,b b
c c,a d
e a a,a a
'''
db['idatas'].append(data)

data={}
data['name']='ref1.csv'
data['text']='''
item
a
c
e
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='複数項目に対して結合する例'
script['comment']='''
'''
script['sh_code']='''
mvcommon vf=items1,items2 K=item m=ref1.csv i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mvcommon(vf="items1,items2", K="item", m="ref1.csv", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='項目名を変更する例'
script['comment']='''
``item2`` に新項目名 ``new2`` を指定しているので、
項目名が変更され出力される。
'''
script['sh_code']='''
mvcommon vf=items1,items2:new2 K=item m=ref1.csv i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mvcommon(vf="items1,items2:new2", K="item", m="ref1.csv", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='項目を追加する例'
script['comment']='''
``item1`` に新項目名 ``new1`` を、
``item2`` に新項目名 ``new2`` を指定し、
``A=True`` オプションを付けているので
新項目 ``new1`` と ``new2`` が追加され出力される。
'''
script['sh_code']='''
mvcommon vf=items1:new1,items2:new2 -A K=item m=ref1.csv i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mvcommon(vf="items1:new1,items2:new2", A=True, K="item", m="ref1.csv", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

