# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mclique'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat.csv'
data['text']='''
node1,node2
a,b
a,c
a,d
a,e
b,c
b,d
b,f
c,d
c,e
d,e
e,f
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
グラフデータ ``dat.csv`` から極大クリークを列挙し ``result.csv`` に出力する。
'''
script['sh_code']='''
mclique.rb ei=dat1.csv ef=node1,node2 o=result.csv
'''
script['py_code']='''
import nysol.take as nt
nt.mclique(ei="dat.csv", ef="node1,node2", o="result.csv")
'''
script['odatas']='result.csv:0'
db['scripts'].append(script)

script={}
script['title']='サイズの指定'
script['comment']='''
サイズが4以上の極大クリークのみ列挙する。
'''
script['sh_code']='''
mclique.rb ei=dat.csv ef=node1,node2 l=4 o=result.csv
'''
script['py_code']='''
import nysol.take as nt
nt.mclique(ei="dat.csv", ef="node1,node2", l=4, o="result.csv")
'''
script['odatas']='result.csv:0'
db['scripts'].append(script)

script={}
script['title']='全クリーク列挙'
script['comment']='''
サイズが4以上の全クリークを列挙する。
'''
script['sh_code']='''
mclique.rb ei=dat.csv ef=node1,node2 l=4 -all o=result.csv
'''
script['py_code']='''
import nysol.take as nt
nt.mclique(ei="dat.csv", ef="node1,node2", l=3, u=3, all=True, o="result.csv")
'''
script['odatas']='result.csv:0'
db['scripts'].append(script)


