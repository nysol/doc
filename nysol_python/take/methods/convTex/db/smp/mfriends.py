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
n1,n2,sim
a,b,0.40
a,c,0.31
a,d,0.31
b,c,0.20
b,d,0.24
b,e,0.14
c,d,0.30
d,e,0.09
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
rank=2の相互類似関係にある辺を選択する。
edge.csvの辺データを見ると、各節点に隣接する節点のうち、
``sim`` が上位2位の隣接節点は次の通りである。
a-(b,c,d)(cとdは同点2位), b-(a,d), c-(a,d), d-(a,c), e-(b,d)。
最初の節点aにとっての1位の節点はbで、逆にbから見てもaは2位に入っているため相互類似関係にあるので、
有向辺a->bを出力する。
一方で、節点bにとっての2位の節点はdであるが、逆にdから見るとbは2位に入っていないので有向辺b->dは出力されない。
このように、上に示した、上位2位の節点-隣接節点について、有向辺の出力判定をして得られた結果が ``output.csv`` に出力される。
'''
script['sh_code']='''
mfriends.rb ei=edge.csv ef=n1,n2 sim=sim rank=2 eo=output.csv
'''
script['py_code']='''
import nysol.take as nt
nt.mfriends(ei="edge.csv", ef="n1,n2", sim="sim", rank=2, eo="output.csv").run()
'''
script['odatas']='output.csv:0'
db['scripts'].append(script)

