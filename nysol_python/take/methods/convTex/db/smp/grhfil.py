# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mitemset'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.graph'
data['text']='''
0 1
0 2
0 4
1 2
1 4
1 6
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
'''
script['py_code']='''
from nysol.take.extcore import grhfil
grhfil(type="ueE_",i="dat1.graph",o="result.graph")
'''
script['odatas']='result.txt:0'
db['scripts'].append(script)

