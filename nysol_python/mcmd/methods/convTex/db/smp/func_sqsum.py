# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='sqsum'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,v1,v2,v3
1,1,2,3
2,-5,2,1
3,1,,3
4,,,
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mcal c='sqsum(${v1},${v2},${v3})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='sqsum(${v1},${v2},${v3})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='ワイルドカードを利用した例'
script['comment']='''
``v`` から始まる項目( ``v1,v2,v3`` )をワイルドカード「 ``v*`` 」によって指定している。
'''
script['sh_code']='''
mcal c='sqsum(${v*})' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='sqsum(${v*})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='-nを利用した例'
script['comment']='''
``v2`` にNULL値を含む ``id=3`` の行の結果もNULLとなる。
'''
script['sh_code']='''
mcal c='sqsum(${v1},${v2},${v3},"-n")' a=rsl i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='sqsum(${v1},${v2},${v3},"-n")', a='rsl', i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

