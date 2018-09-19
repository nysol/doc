# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mdelnull'
db['title']='NULL値行の削除'
db['related']=[
  ["mnullto","NULL値を含む行を削除するのではなく、NULL値を指定の文字列に変換する。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目について、NULL値が含まれる行を削除(撰択)する。\\

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
NULL値の検索対象となる項目名（複数項目指定可）を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
削除(撰択)する単位となるキー項目名（複数項目指定可）を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='出力しない'
param['text']='''
不一致データ出力データを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='bufcount'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
バッファのサイズ数を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='F'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
項目間AND条件
``f=`` パラメータで複数項目を指定した場合、その全ての値がNULL値の行を削除(撰択)する。
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
条件反転
削除ではなく選択する。
'''
db['params'].append(param)

param={}
param['kwd']='R'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
レコード間AND条件
``k=`` パラメータを指定した場合、その全ての行がNULL値の行を削除(撰択)する。
'''
db['params'].append(param)

db['comParams']='i,o,bufcount,assert_diffSize,assert_nullkey,nfn,nfno,x,q,tmppath,precision'
