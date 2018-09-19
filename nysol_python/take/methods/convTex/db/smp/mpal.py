# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mpolishing'

############################### IDATA
db['idatas']=[]

data={}
data['name']='tra.csv'
data['text']='''
id,item
1,a
1,b
2,a
2,b
3,a
3,b
4,b
4,c
5,a
5,c
6,a
6,c
7,d
7,e
8,d
8,e
9,d
9,e
A,d
A,c
B,e
B,b
C,e
C,a
D,f
D,c
E,f
E,b
F,f
F,a
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
最小支持度を1件で指定しているの( ``S=1`` )、全アイテムペアを列挙し、
そこから類似度として支持度( ``sim="S"`` )が相互に1位のアイテムペアのみを選択する。
'''
script['sh_code']='''
mpal.rb i=tra.csv no=node.csv eo=edge.csv tid=id S=1 item=item sim=S rank=1 dir=b
'''
script['py_code']='''
import nysol.take as nt
nt.mpal(i="tra.csv", no="node.csv", eo="edge.csv", tid="id", S=1, item="item", sim="S", rank="1", dir="b").run()
'''
script['odatas']='node.csv,edge.csv'
db['scripts'].append(script)


