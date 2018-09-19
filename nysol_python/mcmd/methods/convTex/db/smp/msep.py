# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='msep'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
item,date,quantity,price
A,20081201,1,10
B,20081201,4,40
A,20081202,2,20
A,20081203,3,30
B,20081203,5,50
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``dat`` という名前のディレクトリを作成し、
そのディレクトリに日付項目値 ``date`` ごとに異なるファイルに出力する。
'''
script['sh_code']='''
msep d='./dat/${date}.csv' -p i=dat1.csv
'''
script['py_code']='''
nm.msep(d="./dat/${date}.csv", p=True, i="dat1.csv").run()
'''
script['odatas']=''
db['scripts'].append(script)

