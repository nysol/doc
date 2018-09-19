# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mmvsim'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
t,x,y
1,14,0.17
2,11,0.2
3,32,0.15
4,13,0.33
5,8,0.1
6,19,0.56
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``x、y`` 項目についてのピアソンの積率相関係数を3期を窓として計算する。
'''
script['sh_code']='''
mmvsim s=t t=3 c=pearson f=x,y a=sim i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mmvsim(s="t", t="3", c="pearson", f="x,y", a="sim", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

