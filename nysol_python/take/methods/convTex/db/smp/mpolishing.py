# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mpolishing'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
node1,node2
a,b
a,c
a,e
b,c
b,e
b,g
c,d
c,g
d,e
e,f
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
類似度をresemblance(sim=R)とし、th=0.4で枝を張り直してグラフ研磨する。
``log1.csv`` を見ると、グラフ情報の表示が繰り返されておりそれが
5回目(dens4など)で終わっており、研磨回数は5回で収束していることがわかる。
'''
script['sh_code']='''
mpolishing.rb ei=dat1.csv ef=node1,node2 sim=R th=0.4 eo=result1.csv log=log1.csv
'''
script['py_code']='''
import nysol.take as nt
from nysol.take import graph as ng
gi=ng.graph(edgeFile="dat1.csv",title1="node1",title2="node2")
go=nt.mpolishing(gi=gi,sim="R",th=0.4,log="log.csv").run()
e=go.edges().run()
print(e)
# [['a', 'b'], ['a', 'c'], ['a', 'e'], ['a', 'g'], ['b', 'c'], ['b', 'e'], ['b', 'g'], ['c', 'e'], ['c', 'g'], ['e', 'g']]
n=go.nodes().run()
print(n)
# [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g']]
'''
script['odatas']='log.csv:0' # ファイル名の後ろの数字は表示行数。0で全行表示
db['scripts'].append(script)

script={}
script['title']='PMIによる研磨'
script['comment']='''
類似度をnormalized PMI(sim=P)とし、th=0.2で枝を張り直して得られた研磨グラフ。
'''
script['sh_code']='''
mpolishing.rb ei=dat1.csv ef=node1,node2 sim=P th=0.2 eo=result2.csv
'''
script['py_code']='''
import nysol.take as nt
from nysol.take import graph as ng
gi=ng.graph(edgeFile="dat1.csv",title1="node1",title2="node2")
go=nt.mpolishing(gi=gi,sim="P",th=0.2).run()
e=go.edges().run()
print(e)
# [['a', 'b'], ['b', 'c'], ['b', 'g'], ['c', 'g'], ['e', 'f']]
'''
script['odatas']=''
db['scripts'].append(script)

script={}
script['title']='intersectionで1回の研磨'
script['comment']='''
類似度をintersection(sim=T)とし、2件以上(th=2)で枝を張り直し
直接の接続を考慮に入れる例。研磨回数は1回のみ(iter=1)。
'''
script['sh_code']='''
mpolishing.rb ei=dat1.csv ef=node1,node2 sim=T th=2 iter=1 eo=result3.csv
'''
script['py_code']='''
import nysol.take as nt
from nysol.take import graph as ng
gi=ng.graph(edgeFile="dat1.csv",title1="node1",title2="node2")
go=nt.mpolishing(gi=gi,sim="T",th=2,iter=1).run()
e=go.edges().run()
print(e)
# [['a', 'b'], ['a', 'c'], ['a', 'd'], ['a', 'e'], ['a', 'g'], ['b', 'c'], ['b', 'd'], ['b', 'e'], ['b', 'g'], ['c', 'd'], ['c', 'e'], ['c', 'g'], ['d', 'e'], ['e', 'f']]
'''
script['odatas']='result.csv'
db['scripts'].append(script)

script={}
script['title']='直接の接続を考慮しない例'
script['comment']='''
``indirect`` オプションを指定することで、類似度の計算で直接の接続は無視される。
出力結果では、枝が全て消えるため、研磨後の枝データは出力されない。
'''
script['sh_code']='''
mpolishing.rb ei=dat1.csv ef=node1,node2 sim=T th=2 eo=result4.csv -indirect
'''
script['py_code']='''
import nysol.take as nt
from nysol.take import graph as ng
gi=ng.graph(edgeFile="dat1.csv",title1="node1",title2="node2")
go=nt.mpolishing(gi=gi,sim="T",th=2,indirect=True).run()
e=go.edges().run()
print(e)
# []
'''
script['odatas']='result.csv'
db['scripts'].append(script)

