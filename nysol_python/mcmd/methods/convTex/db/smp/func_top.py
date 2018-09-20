# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='top'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
val
1
2
3
4
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mcal c='top()' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='top()', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='累計計算の例'
script['comment']='''
'''
script['sh_code']='''
mcal c='if(top(),${val},${val}+#{})' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='if(top(),${val},${val}+#{})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

