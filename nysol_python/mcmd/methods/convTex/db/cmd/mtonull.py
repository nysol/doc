# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mtonull'
db['title']='NULL値へ置換'
db['related']=[
  ["mnullto","逆にNULL値を指定の文字列に置換する。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目を対象に、
``v=`` パラメータで指定した値にマッチした項目データをNULL値に置換する。
マッチの方法としては完全一致(デフォルト)と部分文字列マッチ( ``sub=True`` オプション)を選択できる。

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
置換対象の項目名リスト(複数項目指定可)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='v'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
``f=`` パラメータで指定した項目の値が、ここで指定した文字列リスト(複数項目指定可)
のいずれかにマッチすればNULL値に置換する。
'''
db['params'].append(param)

param={}
param['kwd']='sub'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
部分文字列マッチを行う。
'''
db['params'].append(param)

param={}
param['kwd']='W'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
ワイド文字としてマッチを行う。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullin,nfn,nfno,x,tmppath,precision'
