# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='dist'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,x1,y1,x2,y2
1,0,0,1,1
2,0,1,2,0
3,,,,
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,x1,y1,x2,y2
1,a,b,a,c
2,0,1,0,1
3,,,,
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='ユークリッド距離'
script['comment']='''
'''
script['sh_code']='''
mcal c='dist("euclid",${x1},${y1},${x2},${y2})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='dist("euclid",${x1},${y1},${x2},${y2})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='都市ブロック距離'
script['comment']='''
'''
script['sh_code']='''
mcal c='dist("cityblock",${x1},${y1},${x2},${y2})' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='dist("cityblock",${x1},${y1},${x2},${y2})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='ハミング距離'
script['comment']='''
ハミング距離の計算では、値を文字列として指定していることに注意する。
'''
script['sh_code']='''
mcal c='dist("hamming",$s{x1},$s{y1},$s{x2},$s{y2})' a=rsl i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='dist("hamming",$s{x1},$s{y1},$s{x2},$s{y2})', a='rsl', i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

