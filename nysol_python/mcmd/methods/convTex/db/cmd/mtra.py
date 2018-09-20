# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mtra'
db['title']='縦型データをベクトル項目に変換'
db['related']=[
  ["mvsort","トランザクションデータは、ベクトル型データを処理する一連の処理コマンド( ``mv`` から始まる)によって加工できる。"],
  ["mcross","トランザクションデータとしてではなく、個々のアイテムを独立した項目として出力し、その出現件数を出力する。"],
  ["mtrafld","「項目名=値」の形式でトランザクションデータを作成する。"],
  ["mtraflg","項目名をアイテムとしてトランザクションデータを作成する。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目値をアイテムとし、それらのアイテムを連結し新しいベクトル項目(トランザクション項目とも呼ぶ)として出力する。
アイテムの区切り文字は ``delim=`` パラメータで指定する。

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
ここで指定した項目(複数項目指定可)の値がアイテムとして連結されトランザクション項目となる。
NULL値は無視される。
'''
db['params'].append(param)

param={}
param['kwd']='s'
param['type']='str'
param['mand']=False
param['cond']=' ``q`` オプションの指定がない場合'
param['default']=''
param['text']='''
ここで指定した項目(複数項目指定可)で並べ替えられた後、変換が行われる。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
文字列パターンの単位となる項目名(複数項目指定可)リスト。
``r`` オプションが指定された時は指定できない。
'''
db['params'].append(param)

param={}
param['kwd']='delim'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
ここで指定した文字を区切り文字とする（省略時はスペース）。
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
トランザクション項目を縦型データに変換する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
