# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mnullto'
db['title']='NULL値の置換'
db['related']=[
  ["mdelnull","置換ではなく、行を削除したい場合はこちら。"],
  ["mchgstr","NULL値でなく文字列を置換したい場合に使用する。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目について
NULL値を ``v=`` パラメータで指定した文字列に置換する。

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
ここで指定した項目(複数項目指定可)のNULL値が置換される。
'''
db['params'].append(param)

param={}
param['kwd']='v'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
ここで指定した文字列にNULL値を置換する。
'''
db['params'].append(param)

param={}
param['kwd']='p'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
前の行の値で置換する。
``v=`` パラメータと同時に指定できない。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
``p`` オプションを指定した時にのみ意味があり、ここで指定した項目値の単位で置換処理を行なう。
'''
db['params'].append(param)

param={}
param['kwd']='s'
param['type']='str'
param['mand']=False
param['cond']=' ``q`` オプションの指定がない場合'
param['default']=''
param['text']='''
``p`` オプションを指定した時にのみ意味があり、 ``k=`` 項目内での並び順を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='O'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
NULL値以外を置換したい場合は、ここで値を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='A'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
このオプションにより、指定した項目を置き換えるのではなく、
``A`` オプションを指定した場合は必ず、
:(コロン）で新項目名を指定する必要がある。例）f=数量:置換後の項目名
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,nfn,nfno,x,q,tmppath,precision'
