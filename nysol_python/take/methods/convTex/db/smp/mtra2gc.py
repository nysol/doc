# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mclique'

############################### IDATA
db['idatas']=[]

data={}
data['name']='tra.csv'
data['text']='''
id,item
1,a
1,b
1,c
1,f
2,d
2,e
2,f
3,a
3,b
3,d
3,f
4,b
4,d
4,f
5,a
5,b
5,d
5,e
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
共起頻度が2以上( ``S=2`` )、確信度が0.7以上 (``sim="C"`` , ``th=0.7`` )を満たす2アイテム集合を
グラフデータ(節点データファイル: ``node.csv`` , 辺データファイル: ``edge.csv`` )として列挙する。
'''
script['sh_code']='''
mtra2gc.rb i=tra.csv tid=id item=item S=1 sim=C th=0.7 no=node.csv eo=edge.csv
'''
script['py_code']='''
import nysol.take as nt
nt.mtra2gc(i="tra.csv", tid="id", item="item", S=2, sim="C", th=0.7, no="node.csv", eo="edge.csv").run()
'''
script['odatas']='node.csv:0,edge.csv:0'
db['scripts'].append(script)


