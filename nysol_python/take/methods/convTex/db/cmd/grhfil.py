# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='grhfil'
db['title']='グラフフィルタ'
db['related']=[
]

############################### DOCUMENT
db['doc']='''
グラフの加工を行う。
'''

############################### PARAMETERS
db['params']=[]

param={}
param['kwd']='type'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
	以下に示すパラメータを組み合わせて文字列として指定する(ex. "UeEs")。

	1) グラフタイプ【必須】
	グラフの種類を以下の5つから一つ選んで指定する。

	* B:二部グラフ
	* d:有向グラフ(入力隣接行列を変更しない)
	* D:逆向きの有向グラフ(隣接行列の下三角行列と上三角行列を入れ替える)
	* U:片方向無向グラフ(隣接行列の下三角行列を削除し、重複したエッジを削除する)
	* u:双方向無向グラフ(入力隣接行列の下三角行列と上三角行列を対称にする)

	2) グラフの書式【オプション】
	入出力ファイルのグラフの書式は、隣接行列形式がデフォルトであるが、
	それをノードペアのエッジ形式に変更することができる。

	* e: 入力ファイルをエッジ形式とする。
	* E: 出力ファイルをエッジ形式とする。

	3) その他の指定

	* s: 出力のグラフの隣接ノードを昇順に並べる。
	* S: 出力のグラフの隣接ノードを降順に並べる。
	* n: 入力データの一行目を"ノード数 エッジ数"とする。
	* N: 出力データの一行目に"ノード数 エッジ数"を出力する。
	* v: 入力データのノード番号は1から始まるものとする。
	* V: 出力データのノード番号は1からはじまるものとして出力する。
	* 0: 一列目にノード番号を出力する(出力が隣接行列形式の場合のみ)。
	* w: 入力ファイルの隣接ノードの次の数字を重みとする。
	* W: 出力ファイルの隣接ノードの次に重みを出力する。
	* %:show progress
	* _:no message
	* +:write solutions in append mode

	* v,V:node ID in read/write file starts from 1,
	* q:non-transform mode (valid with -P option)
	* 9:give weight 1 to each vertex ID (with 0)
	* 1:unify consecutive two same numbers into one
'''
db['params'].append(param)

param={}
param['kwd']='i'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
トランザクションファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='o'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
出力ファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='t'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制約なし'
param['text']='''
次数が指定した値より小さいノードは出力しない【デフォルト=制約なし】
'''
db['params'].append(param)

param={}
param['kwd']='T'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制約なし'
param['text']='''
次数が指定した値より大きいノードは出力しない【デフォルト=制約なし】
'''
db['params'].append(param)

param={}
param['kwd']='ideg'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制約なし'
param['text']='''
有向グラフにおいて入次数が指定した値より小さいノードは出力しない
'''
db['params'].append(param)

param={}
param['kwd']='Ideg'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制約なし'
param['text']='''
有向グラフにおいて入次数が指定した値より大きいノードは出力しない
'''
db['params'].append(param)

param={}
param['kwd']='odeg'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制約なし'
param['text']='''
有向グラフにおいて出次数が指定した値より小さいノードは出力しない
'''
db['params'].append(param)

param={}
param['kwd']='Odeg'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制約なし'
param['text']='''
有向グラフにおいて出次数が指定した値より大きいノードは出力しない
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']="float"
param['mand']=False
param['cond']=''
param['default']='制約なし'
param['text']='''
重みが指定した値より小さいエッジは出力しない
'''
db['params'].append(param)

param={}
param['kwd']='R'
param['type']="float"
param['mand']=False
param['cond']=''
param['default']='制約なし'
param['text']='''
重みが指定した値より大きいエッジは出力しない
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='データ上の最大番号+1'
param['text']='''
ノードの個数を与える
'''
db['params'].append(param)

param={}
param['kwd']='w'
param['type']="bool"
param['mand']=False
param['cond']=''
param['default']='均等な重みを使う'
param['text']='''
入力ファイルの3項目目を重みとして読み込む(3項目目がなければ0がセットされる)
'''
db['params'].append(param)

param={}
param['kwd']='W'
param['type']="bool"
param['mand']=False
param['cond']=''
param['default']='ファイル出力しない'
param['text']='''
出力ファイルの3項目目に重みを出力する
'''
db['params'].append(param)

param={}
param['kwd']='d'
param['type']="bool"
param['mand']=False
param['cond']=''
param['default']='ファイル出力しない'
param['text']='''
指定したグラフとの差異を出力する(gTypeとgFormatは同じでなければならない)
'''
db['params'].append(param)

param={}
param['kwd']='dth'
param['type']="float"
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
specify the threshold value (d=が必要)
'''
db['params'].append(param)

param={}
param['kwd']='m'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
指定したグラフとのintersectionを出力する(gTypeとgFormatは同じでなければならない)
'''
db['params'].append(param)

param={}
param['kwd']='M'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
指定したグラフとのunionを出力する(gTypeとgFormatは同じでなければならない)
'''
db['params'].append(param)

param={}
param['kwd']='P'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
permute the vertex ID to coutinuous numbering and output the permutation table to the file
'''
db['params'].append(param)

param={}
param['kwd']='Q'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
permute the numbers in the file according to the table 
'''
db['params'].append(param)


db['comParams']=''
