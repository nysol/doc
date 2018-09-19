# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mfsort'
db['title']='項目ソート'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
各行で ``f=`` で指定した複数項目の値を並べ替え(デフォルトでは文字列昇順)、その順序で出力する。
項目名の並びは変化しないことに注意する。

'''

############################### PARAMETERS
db['params']=[]

param={}
param['kwd']='i'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='標準入力'
param['text']='''
入力データを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='o'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='標準出力'
param['text']='''
出力データを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
ソート対象となる項目を複数指定する。単一の項目を指定してもよいが、結果は変わらない。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
数値順に並べる。
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
逆順に並べる。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullin,nfn,nfno,x,tmppath,precision'
