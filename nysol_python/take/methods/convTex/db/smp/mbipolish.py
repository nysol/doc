# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mpolishing'

############################### IDATA
db['idatas']=[]

data={}
data['name']='edge.csv'
data['text']='''
node1,node2
A,a
A,b
B,a
B,b
C,c
C,d
D,b
D,e
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mbipolish.rb ei=edge.csv ef=node1,node2 th=0.2 eo=output.csv
'''
script['py_code']='''
import nysol.take as nt
nt.mbipolish(ei="edge.csv",ef="node1,node2", th=0.2, eo="output.csv").run()
'''
script['odatas']='output.sv:0' # ファイル名の後ろの数字は表示行数。0で全行表示
db['scripts'].append(script)

