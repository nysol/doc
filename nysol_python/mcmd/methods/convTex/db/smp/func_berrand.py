# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='berrand'

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
script['title']='基本例'
script['comment']='''
確率$p=0.2$のベルヌーイ乱数を生成する。
乱数の種を指定しているので、何度実行しても同じ乱数系列が生成される。
'''
script['sh_code']='''
mcal c='berrand(0.2,111)' a=rand i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='berrand(0.2,111)', a='rand', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='0,1の整数乱数'
script['comment']='''
0と1の2種類の整数乱数を生成する。
乱数の種を指定していないので、実行の度に異なる乱数系列が生成される。
'''
script['sh_code']='''
mcal c='randi(0,1)' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='randi(0,1)', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

