# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='match'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,f1,f2,f3
1,1,1,1
2,1,0,1
3,,,
4,1,,1
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,s1,s2,s3
1,ab,abx,x
2,abc,xaby,xxab
3,,,
4,#ac,x,x
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='OR完全一致'
script['comment']='''
``f1,f2,f3`` 項目のいずれかが ``1`` であれば真を返す。
'''
script['sh_code']='''
mcal c='match("1",$s{f1},$s{f2},$s{f3})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='match("1",$s{f1},$s{f2},$s{f3})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='AND完全一致'
script['comment']='''
``f1,f2,f3`` 項目の全てが文字列 ``"1"`` であれば真を返す。
'''
script['sh_code']='''
mcal c='matcha("1",$s{f1},$s{f2},$s{f3})' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='matcha("1",$s{f1},$s{f2},$s{f3})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='OR部分一致'
script['comment']='''
``s1,s2,s3`` 項目のいずれかが、文字列 ``ab`` を含んでいれば真を返す。
'''
script['sh_code']='''
mcal c='matchs("ab",$s{s1},$s{s2},$s{s3})' a=rsl i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='matchs("ab",$s{s1},$s{s2},$s{s3})', a='rsl', i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='AND部分一致'
script['comment']='''
文字列 ``ab`` が ``s1,s2,s3`` 項目の全てに、文字列 ``ab`` が含まれて入れば真を返す。
'''
script['sh_code']='''
mcal c='matchas("ab",$s{s1},$s{s2},$s{s3})' a=rsl i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.mcal(c='matchas("ab",$s{s1},$s{s2},$s{s3})', a='rsl', i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='NULL値の検索'
script['comment']='''
``str`` 項目がNULL値であれば真を返す。
'''
script['sh_code']='''
mcal c='match(nulls(),$s{s1},$s{s2},$s{s3})' a=rsl i=dat2.csv o=rsl5.csv
'''
script['py_code']='''
nm.mcal(c='match(nulls(),$s{s1},$s{s2},$s{s3})', a='rsl', i="dat2.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

