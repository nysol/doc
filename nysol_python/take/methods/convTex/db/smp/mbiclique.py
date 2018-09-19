# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mitemset'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat.csv'
data['text']='''
node1,node2
a,A
a,B
a,C
b,A
b,B
b,D
c,A
c,D
d,B
d,C
d,D
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
2部グラフデータ ``dat.csv`` から極大2部クリークを列挙し ``result.csv`` に出力する。
'''
script['sh_code']='''
mbiclique.rb ei=dat.csv ef=node1,node2 o=result.csv
'''
script['py_code']='''
import nysol.take as nt
nt.mbiclique(ei="dat.csv", ef="node1,node2", o="result.csv").run()
'''
script['odatas']='result.csv:0'
db['scripts'].append(script)

script={}
script['title']='サイズを制限する例'
script['comment']='''
項目 ``node1,node2`` 共にサイズが2の極大二部クリークを列挙する。
'''
script['sh_code']='''
mbiclique.rb ei=dat.csv ef=node1,node2 o=result.csv l=2,2 u=2,2
'''
script['py_code']='''
import nysol.take as nt
nt.mbiclique(ei="dat.csv", ef="node1,node2", l="2,2",u="2,2", o="result.csv").run()
'''
script['odatas']='result.csv:0'
db['scripts'].append(script)

script={}
script['title']='エッジ形式での出力'
script['comment']='''
``edge=True`` によって、出力形式がエッジ形式(ノードペア)になる。
'''
script['sh_code']='''
mbiclique.rb ei=dat.csv ef=node1,node2 o=result.csv l=2,2 u=2,2
'''
script['py_code']='''
import nysol.take as nt
nt.mbiclique(ei="dat.csv", ef="node1,node2", l="2,2",u="2,2", edge=True, o="result.csv").run()
'''
script['odatas']='result.csv:0'
db['scripts'].append(script)


script={}
script['title']='部分的にサイズを制限する例'
script['comment']='''
項目 ``node1`` のサイズの下限を1に(デフォルトの下限が1なので実際には意味がないが指定例として)、
項目 ``node2`` のサイズの上限を3に制限した極大二部クリークを列挙する。
``u=` パラメータの1番目の値がnullになっているのは、項目 ``node1`` の上限を設定しないためである。
'''
script['sh_code']='''
mbiclique.rb ei=dat.csv ef=node1,node2 o=result3.csv l=1, u=,3
'''
script['py_code']='''
import nysol.take as nt
nt.mbiclique(ei="dat.csv", ef="node1,node2", l="1,",u=",3", o="result.csv").run()
'''
script['odatas']='result.csv:0'
db['scripts'].append(script)

