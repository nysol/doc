# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='medset'
db['title']='アイテム集合の共通集合'
db['related']=[
]

############################### DOCUMENT
db['doc']='''
アイテム集合の共通集合を列挙する。
'''

############################### PARAMETERS
db['params']=[]

param={}
param['kwd']='ci'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
cluster-filename
'''
db['params'].append(param)

param={}
param['kwd']='si'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
set-filename
'''
db['params'].append(param)

param={}
param['kwd']='th'
param['type']="int"
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
threshold
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
param['kwd']='H'
param['type']="bool"
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
do not use histgram, just output the items
'''
db['params'].append(param)

param={}
param['kwd']='R'
param['type']="bool"
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
do not output singleton clusters
'''
db['params'].append(param)

param={}
param['kwd']='V'
param['type']="bool"
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
output ratio of appearances of all items
'''
db['params'].append(param)

param={}
param['kwd']='T'
param['type']="bool"
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
clustering by connected component (read edge type file)
'''
db['params'].append(param)

param={}
param['kwd']='I'
param['type']="bool"
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
find an independent set, and clustering by using the vertices in it as seeds 
(read edge type files)
'''
db['params'].append(param)

param={}
param['kwd']='i'
param['type']="bool"
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
output for each item, ratio of records including the item
'''
db['params'].append(param)

param={}
param['kwd']='t'
param['type']="bool"
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
transpose the input database, (transaction will be item, and vice varsa)
'''
db['params'].append(param)

param={}
param['kwd']='l'
param['type']="int"
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
output clusters of size at least [num]
'''
db['params'].append(param)

param={}
param['kwd']='progress'
param['type']="bool"
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
show progress
'''
db['params'].append(param)

param={}
param['kwd']='nomsg'
param['type']="bool"
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
no message
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
