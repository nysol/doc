# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='sspc'
db['title']='アイテム集合のクラスタリング'
db['related']=[
]

############################### DOCUMENT
db['doc']='''
実装の詳細は |simsetorg| を参照されたい。

  .. |simsetorg| raw:: html

		<a href="http://research.nii.ac.jp/~uno/code/simset.html" target="_blank">simsetのオリジナル解説ページ</a>
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
* _:no message
* +:write solutions in append mode
* =:do not remove temporal files
* @:do not execute data polishing, E:read edge list file
* i:set similarity measure to the ratio of one is included in the other
* I:set similarity measure to the ratio of both are included in the other
* S:set similarity measure to :math:`|A\cap B|/max(|A|,|B|)`
* s:set similarity measure to :math:`|A\cap B|/min(|A|,|B|)`
* C:set similarity measure to the cosign distance, the inner product of the normalized characteristic vectors
* T:set similarity measure to the intersection size, i.e., :math:`|A\cap B|`
* R:(recemblance) set similarity measure to :math:`|A\cap B|/|A\cup B|`
* P(PMI): set similarity measure to :math:`log(|A\cap B|*|all| / (|A|*|B|))` where :math:`|all|` is the number of all items
* M:output intersection of each clique, instead of IDs of its members
* v (with M): output ratio of records, including each item
* m:do not remove edges in the data polishing phase
* O:repeatedly similarity clustering until convergence
* Y:take intersection of original graph and polished graph, instead of clique mining
* 1:do not remove the same items in a record (with -G)
* W:load weight of each element
* t:transpose the input database, so that each line will be considered as a record
'''
db['params'].append(param)

param={}
param['kwd']='i'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
similarity-graph-filename
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
param['kwd']='th_s'
param['type']="float"
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
similarity-threshold
'''
db['params'].append(param)

param={}
param['kwd']='th_d'
param['type']="int"
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
degree-threshold
'''
db['params'].append(param)

param={}
param['kwd']='G'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
use [similarity] of [threshold] in the first phase (file is regarded as a transaction database)
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
find only k-best for each record in ``G`` option
'''
db['params'].append(param)

param={}
param['kwd']='M'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
merge similar cliques of similarity in [num] of recemblance (changes to 'x' by giving '-Mx')
'''
db['params'].append(param)

param={}
param['kwd']='m'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
take independently cliques from similar cliques of similarity in [num] of recemblance, 
and merge the neighbors of each independent clique ('recemblance' changes to 'x' by giving '-Mx')
'''
db['params'].append(param)

param={}
param['kwd']='v'
param['type']="float"
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
specify majority threshold (default=0.5) 
(if negative is given, items of frequency no more than -[num] are output)
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
ignore vertices of degree more than [num]
'''
db['params'].append(param)

param={}
param['kwd']='l'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
ignore vertices of degree less than [num]
'''
db['params'].append(param)

param={}
param['kwd']='U'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='上限なし'
param['text']='''
ignore transactions of size more than [num] (with -G)
'''
db['params'].append(param)

param={}
param['kwd']='L'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='上限なし'
param['text']='''
ignore transactions of size less than [num] (with -G)
'''
db['params'].append(param)

param={}
param['kwd']='I'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='上限なし'
param['text']='''
ignore items of frequency more than [num] (with -G)
'''
db['params'].append(param)

param={}
param['kwd']='i'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='上限なし'
param['text']='''
ignore items of frequency less than [num] (with -G)
'''
db['params'].append(param)

param={}
param['kwd']='II'
param['type']="float"
param['mand']=False
param['cond']=''
param['default']='上限なし'
param['text']='''
give thresholds by the ratio of #ransactions/#items)
'''
db['params'].append(param)

param={}
param['kwd']='ii'
param['type']="float"
param['mand']=False
param['cond']=''
param['default']='上限なし'
param['text']='''
give thresholds by the ratio of #ransactions/#items)
'''
db['params'].append(param)

param={}
param['kwd']='t'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='上限なし'
param['text']='''
ignore pairs whose intersection size is less than [num] (T for first phase with -G option, and t for polishing)
'''
db['params'].append(param)

param={}
param['kwd']='T'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='上限なし'
param['text']='''
ignore pairs whose intersection size is more than [num] (T for first phase with -G option, and t for polishing)
'''
db['params'].append(param)

param={}
param['kwd']='O'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
specify the number of repetitions
'''
db['params'].append(param)

param={}
param['kwd']='9'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
shrink records of similarity more than [num]
'''
db['params'].append(param)

param={}
param['kwd']='X'
param['type']="float"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
multiply the weight by [num] (and trancate by 1, for C command)
'''
db['params'].append(param)

param={}
param['kwd']='x'
param['type']="float"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
power the weight by [num] (and normalize, for C command)
'''
db['params'].append(param)

param={}
param['kwd']='y'
param['type']="float"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
at last, remove edges with weight less than [num]
'''
db['params'].append(param)

param={}
param['kwd']='w'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']='重みは等しいものとする'
param['text']='''
load weight of elements from the file
'''
db['params'].append(param)

param={}
param['kwd']='multi'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='1'
param['text']='''
use multicores of [num] (compile by 'make multicore')
'''
db['params'].append(param)

param={}
param['kwd']='W'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
specify the working directory (folder). 
The last letter of the directory has to be '/' ('\')
'''
db['params'].append(param)

param={}
param['kwd']='separator'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']='スペース'
param['text']='''
give the separator of the numbers in the output
'''
db['params'].append(param)

param={}
param['kwd']='Q'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']='replaceしない'
param['text']='''
replace the output numbers according to the permutation table given by [filename]
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
