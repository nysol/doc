# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='msed'
db['title']='正規表現による文字列置換'
db['related']=[
  ["mchgstr","単純な文字列マッチによる置換であればこのコマンドを利用する。"],
  ["mcal","正規表現を扱う関数がいくつか用意されている。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目について、
``c=`` パラメータで指定した正規表現に一致する内容を
``v=`` パラメータ指定した文字列で置換する。

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
置換対象となる項目名リスト(複数項目指定可)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='c'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
置換したい文字列についての正規表現を指定する。
正規表現の使用方法参照
'''
db['params'].append(param)

param={}
param['kwd']='v'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
``c=`` パラメータで指定した正規表現にマッチした部分文字列が、
ここで指定した文字列に置換される。
マッチ結果を用いた置換も可能で、指定方法は以下の通り。
\verb|$
``$```  : 置換対象文字列の先頭から、マッチした文字列の直前までの文字列
``$'``  : マッチした文字列の直後から、置換対象文字列の最後までの文字列
``$N``  : N番目の部分マッチ文字列( ``N>=1`` )
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
新たに項目が追加される。
'''
db['params'].append(param)

param={}
param['kwd']='g'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
正規表現にマッチする全ての部分文字列を置換対象とする。
'''
db['params'].append(param)

param={}
param['kwd']='W'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
ワイド文字として正規表現による文字列置換を行う。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
