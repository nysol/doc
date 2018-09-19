# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mace'
db['title']='極大クリークの列挙'
db['related']=[
]

############################### DOCUMENT
db['doc']='''
実装の詳細は |maceorg| を参照されたい。

  .. |maceorg| raw:: html

		<a href="http://research.nii.ac.jp/~uno/code/mace.html" target="_blank">maceのオリジナル解説ページ</a>
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
列挙するクリークのタイプ(C|M)、及び出力形式を文字列として指定する。
クリークのタイプとして以下の2つから一つを選ぶ。

* C:クリーク
* M:極大クリーク

また出力形式として以下の組み合わせで指定する。
	
* e:エッジリストとして出力する。
* _:メッセージを出力しない。
* +:出力を追記する。
'''
db['params'].append(param)

param={}
param['kwd']='i'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
入力データファイル名(隣接行列形式)を指定する。
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
param['kwd']='l'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
クリークのサイズの下限値を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
クリークのサイズの上限値を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='S'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
ここで指定した数のクリークを出力したら停止する。
'''
db['params'].append(param)

param={}
param['kwd']='separator'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']='スペース'
param['text']='''
入力データの区切り文字を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='i'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
replace the output numbers according to the permutation table given by [filename]
'''
db['params'].append(param)

db['comParams']=''
