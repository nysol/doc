# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='lcm'
db['title']='Linear time Closed itemset Miner'
db['related']=[
]

############################### DOCUMENT
db['doc']='''
実装の詳細は |lcmorg| を参照されたい。

  .. |lcmorg| raw:: html

		<a href="http://research.nii.ac.jp/~uno/code/lcm.html" target="_blank">lcmのオリジナル解説ページ</a>
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
列挙するアイテム集合のタイプ(F|C|M)、及び出力形式を文字列として指定する。
アイテム集合のタイプとして以下の３つから一つを選ぶ。

* F:頻出アイテム集合
* C:飽和アイテム集合
* M:極大アイテム集合

また出力形式として以下の組み合わせで指定する。
	
* f:アイテム集合の後ろに出現件数を出力する。
* Q:アイテム集合の前に出現件数を出力する。
* I:アイテム集合の次の行に出現集合(出現するトランザクション行番号)を出力する。
* t:トランザクションデータベースを転置する(アイテムiはi番目のトランザクションとなり、j番目のトランザクションはアイテムjとなる)。
* A:w=でプラスとマイナスのトランザクションの重みを指定した場合、プラス/マイナスそれぞれの件数とその比を出力する。
* P:positive-closed itemset mining
* R:output redundant items for rule mining (usually, redundant items are removed, to be minimal, in the case of rule mining)
* i:do not output itemset to the output file (only rules)
* s:output confidence and item frequency by absolute values

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
param['kwd']='sup'
param['type']="int"
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
最小サポートを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='U'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='上限なし'
param['text']='''
最大サポートを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='K'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
頻出な上位のアイテム集合のみ出力する
'''
db['params'].append(param)

param={}
param['kwd']='l'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
アイム集合のサイズの下限値を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
アイム集合のサイズの上限値を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='w'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']='全トランザクションの重みは等しいものとする'
param['text']='''
トランザクションの重みファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='a'
param['type']="float(0以上1以下)"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
相関ルールマイニングを実施しconfidenceの下限値を与える。
'''
db['params'].append(param)

param={}
param['kwd']='A'
param['type']="float(0以上1以下)"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
相関ルールマイニングを実施しconfidenceの上限値を与える。
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']="float(0以上1以下)"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
相関ルールマイニングを実施しrelational confidenceの下限値を与える。
'''
db['params'].append(param)

param={}
param['kwd']='R'
param['type']="float(0以上1以下)"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
相関ルールマイニングを実施しrelational confidenceの上限値を与える。
'''
db['params'].append(param)

param={}
param['kwd']='item'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
指定した番号のアイテムに関する相関ルールを出力する。
'''
db['params'].append(param)

param={}
param['kwd']='so'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']='ファイル出力しない'
param['text']='''
標準出力の内容を指定のファイルに出力する。
'''
db['params'].append(param)

param={}
param['kwd']='separator'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']='スペース'
param['text']='''
出力時のアイテムの区切り文字を指定する。
'''
db['params'].append(param)

db['comParams']=''
