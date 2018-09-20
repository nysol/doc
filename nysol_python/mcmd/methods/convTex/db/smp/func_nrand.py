# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='nrand'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id
1
2
3
4
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='例1: 基本例'
script['comment']='''
平均 0 標準偏差 1(標準正規分布) に基づく乱数を成する。また、乱数の種は 10 に設定している。
'''
script['sh_code']='''
mcal c='nrand(0,1,10)' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='nrand(0,1,10)', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

