# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='msel'
db['title']='条件式による行選択'
db['related']=[
  ["mselnum","簡単な数値範囲による行選択はこちら。"],
  ["mselstr","簡単な文字列マッチによる行選択はこちら。"],
  ["mcal","行選択でなく、計算の結果を項目として出力する。"]
]

############################### DOCUMENT
db['doc']='''
``c=`` パラメータで指定した計算式で計算をおこない、結果が真であれば、その行を選択する。
なおmcalと同じ計算式が利用できるので、詳細は :doc:`mcal` を参照されたい。

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
param['kwd']='c'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
用意された関数を組み合わせて計算する式を指定する。
詳細は :doc:`mcal` を参照。
'''
db['params'].append(param)

param={}
param['kwd']='o'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='標準出力'
param['text']='''
指定の条件に一致する行を出力するデータを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='出力しない'
param['text']='''
指定の条件に一致しない行を出力するデータを指定する。
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
選択ではなく削除する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,nfn,nfno,x,tmppath,precision'
