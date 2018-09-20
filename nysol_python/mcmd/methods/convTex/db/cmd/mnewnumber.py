# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mnewnumber'
db['title']='連番データの新規生成'
db['related']=[
  ["mnewrand","新たに乱数を生成する。"],
  ["mnewstr","固定文字列を生成する。"]
]

############################### DOCUMENT
db['doc']='''
``S=`` パラメータで指定した開始数値もしくはアルファベットにより、
``I=`` パラメータで指定した間隔で連番もしくはアルファベット連番を新規作成し、 ``a=`` パラメータで指定した項目名で出力する。
アルファベット連番とは、AからZの26文字を用いた26進数のこと(A,B, :math:`\cdots` ,Z,AA,AB, :math:`\cdots` ,AZ,BA,BB, :math:`\cdots` ,ZZ,AAA,AAB, :math:`\cdots` )。

'''

############################### PARAMETERS
db['params']=[]

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
param['kwd']='a'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
新規に作成する連番行の項目名を指定する。
``nfn`` もしくは ``nfno`` オプション指定時は指定の必要はない。
'''
db['params'].append(param)

param={}
param['kwd']='I'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='1'
param['text']='''
連番をふる間隔を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='S'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='1'
param['text']='''
開始数値/アルファベット(大文字)
連番の開始数値もしくはアルファベットを指定する。
数値を指定した場合は数値の連番がふられる。
アルファベットを指定した場合はアルファベット連番がふられる。(小文字は指定できない)
'''
db['params'].append(param)

param={}
param['kwd']='l'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='10'
param['text']='''
作成するデータ行数を指定する。
'''
db['params'].append(param)

db['comParams']='o,nfn,nfno,x,tmppath,precision'
