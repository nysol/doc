# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mfsort'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,v1,v2,v3
1,b,a,c
2,a,b,a
3,b,,e
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='例1: 基本例'
script['comment']='''
各行において  ``v1,v2,v3``  の値を昇順にならべ、その順番で  ``v1,v2,v3``  項目として出力する。
'''
script['sh_code']='''
mfsort f=v* i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mfsort(f="v*", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='例2: 降順'
script['comment']='''
降順にしたければ ``r=True`` を付ける。
'''
script['sh_code']='''
mfsort f=v* -r i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mfsort(f="v*", r=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

