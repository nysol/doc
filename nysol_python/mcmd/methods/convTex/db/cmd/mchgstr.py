# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mchgstr'
db['title']='文字列の置換'
db['related']=[
  ["mchgnum","数値範囲による置換ならばこちら。"],
  ["msed","正規表現による置換が可能。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目について、
``c=`` パラメータで指定した置換条件で文字列を置換する。

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
param['kwd']='c'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
置換対象となる文字列と置換文字列を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
ここで指定した項目(複数項目指定可)の文字列を ``c=`` パラメータで指定した置換条件リストに従って置換する。
'''
db['params'].append(param)

param={}
param['kwd']='O'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='null値'
param['text']='''
``c=`` パラメータで指定した置換条件リストのいずれとも合致しない値を
置換するときの文字列(指定がなければNULL値となる)を指定する。
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
'''
db['params'].append(param)

param={}
param['kwd']='F'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``c=`` パラメータで指定した置換条件リストのいずれとも合致しない値は、
その項目の値のまま出力する。
'''
db['params'].append(param)

param={}
param['kwd']='sub'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
検索を完全一致ではなく部分文字列マッチで比較する
すなわち、 ``f=`` パラメータで指定した項目の値に、
``c=`` パラメータで指定した置換条件で文字列を置換する。
'''
db['params'].append(param)

param={}
param['kwd']='W'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``sub=True`` オプションが指定されているときにワイド文字として部分文字列マッチをおこなう。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
