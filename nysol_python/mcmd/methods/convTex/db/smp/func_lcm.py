# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='lcm'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,val1,val2
1,5,3
2,12,4
3,,
4,5.1,3.1
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mcal c='lcm(${val1},${val2})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='lcm(${val1},${val2})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='定数を与える例'
script['comment']='''
val1項目と15の最小公倍数を求める。
'''
script['sh_code']='''
mcal c='lcm(${val1},15)' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='lcm(${val1},15)', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

