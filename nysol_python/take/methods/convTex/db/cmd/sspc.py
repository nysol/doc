# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='sspc'
db['title']='類似アイテムペア列挙'
db['related']=[
]

############################### DOCUMENT
db['doc']='''
実装の詳細は |sspcorg| を参照されたい。

  .. |sspcorg| raw:: html

		<a href="http://research.nii.ac.jp/~uno/code/sspc.html" target="_blank">sspcのオリジナル解説ページ</a>
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
* #:count the number of similar records for each record
* i(inclusion): find pairs [ratio] of items (weighted sum) of one is included in the other (1st is included in 2nd)
* I(both-inclusion): find pairs s.t. the size (weight sum) of intersection is [ratio] of both
* S:set similarity measure to :math:`|A\cap B| / max{|A|,|B|}`
* s:set similarity measure to :math:`|A\cap B| / min{|A|,|B|}`
* T(intersection): find pairs having common [threshld] items
* R(resemblance): find pairs s.t. :math:`|A\cap B|/|A\cup B| >= [threshld]`
* P(PMI): set similarity measure to :math:`log(|A\cap B|*|all| / (|A|*|B|))` where :math:`|all|` is the number of all items
* C(cosign distance): find pairs s.t. inner product of their normalized vectors >= [threshld]
* f,Q:output ratio/size of pairs following/preceding to the pairs
* D:the first entry is ID, and unify the records with the same ID
* N:normalize the ID of latter sets, in -c mode
* n:do not consider a and b in the set when comparing a and b
* Y(y):output elements of each set that contribute to no similarity (y:fast with much memory use)
* 1:remove duplicated items in each transaction
* t:transpose the database so that i-th transaction will be item i
* E:input column-row representation
* w:load weight of each item in each row (with E command)
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
param['kwd']='th'
param['type']="float"
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
``type=`` で指定した類似度の閾値を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='K'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
output [num] pairs of most large similarities
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
output [num] elements of most large similarities, for each element
'''
db['params'].append(param)

param={}
param['kwd']='l'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
ignore transactions with size (weight sum) less than [num]
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
ignore transactions with size (weight sum) more than [num]
'''
db['params'].append(param)

param={}
param['kwd']='L'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
ignore items appearing less than [num]
'''
db['params'].append(param)

param={}
param['kwd']='U'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
ignore items appearing more than [num]
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
param['kwd']='W'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']='重みを使わない'
param['text']='''
read item weights in each row from [filename]
'''
db['params'].append(param)

param={}
param['kwd']='c'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
compare transactions of IDs less than num and the others 
(if 0 is given, automatically set to the boundary of the 1st and 2nd file)
ignore items appearing more than [num]
'''
db['params'].append(param)

param={}
param['kwd']='b'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
ignore pairs having no common item of at least [num]th frequency
'''
db['params'].append(param)

param={}
param['kwd']='B'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
ignore pairs having no common item of frequency at most [num]
'''
db['params'].append(param)

param={}
param['kwd']='T'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
ignore pairs whose intersection size is less than [num]
'''
db['params'].append(param)

param={}
param['kwd']='TT'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
``T=`` with outputting intersection size to the 1st column of each line
'''
db['params'].append(param)

param={}
param['kwd']='stop'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
ここで指定した数のパターンを出力したら停止する。
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

db['comParams']=''
