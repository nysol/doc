# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='lcmseq'
db['title']='系列パターン列挙'
db['related']=[
]

############################### DOCUMENT
db['doc']='''
実装の詳細は |lcmseqorg| を参照されたい。

  .. |lcmseqorg| raw:: html

		<a href="http://research.nii.ac.jp/~uno/code/lcm_seq.html" target="_blank">lcmseqのオリジナル解説ページ</a>
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
* %:show progress
* _:no message
* +:write solutions in append mode
* F:position occurrence
* C:document occurrence
* m:output extension maximal patterns only
* c:output extension closed patterns only
* f,Q:output frequency following/preceding to each output sequence
* A:output coverages for positive/negative transactions
* I(J):output ID's of transactions including each pattern, 
* if J is given, an occurrence is written in a complete stype; transaction ID, starting position and ending position
* i:do not output itemset to the output file (only rules)
* s:output confidence and item frequency by absolute values
* t:transpose the input database (item i will be i-th transaction, and i-th transaction will be item i)
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
param['kwd']='g'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
ギャップ長の上限を与える。
'''
db['params'].append(param)

param={}
param['kwd']='G'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
パターンを含む窓幅の上限を与える。
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
param['kwd']='f'
param['type']="float(0以上1以下)"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
output sequences with frequency no less than [ratio] times 
the frequency given by the product of appearance probability of each item
'''
db['params'].append(param)

param={}
param['kwd']='F'
param['type']="float(0以上1以下)"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
output sequences with frequency no greater than [ratio] times 
the frequency given by the product of appearance probability of each item
'''
db['params'].append(param)

param={}
param['kwd']='p'
param['type']="float(0以上1以下)"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
output sequence only if (frequency)/(abusolute frequency) is no less than [num]
'''
db['params'].append(param)

param={}
param['kwd']='P'
param['type']="float(0以上1以下)"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
output sequence only if (frequency)/(abusolute frequency) is no greater than [num]
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
output sequence only if its negative frequency is no less than [num] 
(negative frequency is the sum of weights of transactions having negative weights)
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
output sequence only if its negative frequency is no greater than [num] 
(negative frequency is the sum of weights of transactions having negative weights)
'''
db['params'].append(param)

param={}
param['kwd']='opos'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
output sequence only if its positive frequency is no less than [num] 
(positive frequency is the sum of weights of transactions having positive weights)
'''
db['params'].append(param)

param={}
param['kwd']='Opos'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
output sequence only if its positive frequency is no greater than [num] 
(positive frequency is the sum of weights of transactions having positive weights)
'''
db['params'].append(param)

param={}
param['kwd']='s'
param['type']="float"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
output itemset rule (of the form (a,b,c) => (d,e)) with confidence at least [num] 
(only those whose frequency of the result is no less than the support)
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
param['kwd']='q'
param['type']="str"
param['mand']=False
param['cond']=''
param['default']='出力なし'
param['text']='''
replace the output numbers according to the permutation table given by [filename]
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
