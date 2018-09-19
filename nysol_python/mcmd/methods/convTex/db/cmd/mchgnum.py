# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mchgnum'
db['title']='数値範囲による置換'
db['related']=[
  ["mchgstr","文字列の置換であればこちら。"],
  ["msed","正規表現を使った置換が可能。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目について、 ``R=`` パラメータで指定する
数値範囲条件と ``v=`` パラメータで指定する置換文字列により、項目の値を置換する。

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
ここで指定した項目(複数項目指定可)の数値を ``R=`` と ``v=`` パラメータで指定した
数値範囲リストおよび置換文字列リストに従って置換する。
'''
db['params'].append(param)

param={}
param['kwd']='R'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
置換対象となる数値範囲を指定(複数項目指定可)する( ``1.1,2.5``  : 1.1以上2.5未満)。
最小値、最大値として ``MIN,MAX`` を使うことができる( ``MIN,2.5``  : 2.5未満)。
'''
db['params'].append(param)

param={}
param['kwd']='O'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='null値'
param['text']='''
範囲外文字列
``R=`` パラメータで指定した数値範囲リストのいずれとも合致しない値を
置換するときの文字列(指定がなければNULL値となる)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='F'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
範囲外を項目の値として出力
``R=`` パラメータで指定した数値範囲リストのいずれとも
合致しない値は、その項目の値のまま出力する。
'''
db['params'].append(param)

param={}
param['kwd']='v'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
``R=`` パラメータで指定した数値範囲に対応する置換文字列を指定する。
``R=`` で指定した値の個数より1つ少い個数でなければならない。
'''
db['params'].append(param)

param={}
param['kwd']='A'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
このオプションにより、指定した項目を置き換えるのではなく、新たに項目が追加される。
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``R=`` パラメータの範囲を'〜より大きく〜以下'として扱う。
例えば、 ``1.1_2.5`` は「1.1より大きく2.5以下」として扱う。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
