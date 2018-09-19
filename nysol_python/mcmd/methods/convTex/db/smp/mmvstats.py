# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mmvstats'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,value
1,5
2,1
3,3
4,4
5,4
6,6
7,1
8,4
9,7
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
移動窓の合計を計算する。
最初の行は期数に満たないため出力されない。
'''
script['sh_code']='''
mmvstats s=id f=value t=2 c=sum i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mmvstats(s="id", f="value", t="2", c="sum", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

