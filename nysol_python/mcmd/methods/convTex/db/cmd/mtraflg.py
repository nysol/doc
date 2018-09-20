# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mtraflg'
db['title']='クロス表をトランザクション項目に変換'
db['related']=[
  ["mvsort","トランザクションデータはベクトル型データを処理する一連の処理コマンド( ``mv`` から始まる)によって加工できる。"],
  ["mcross","トランザクションデータとしてではなく、個々のアイテムを独立した項目として出力し、その出現件数を出力する。"],
  ["mtra","項目の値をアイテムとしてトランザクションデータを作成する。"],
  ["mtrafld","「項目名=値」の形式でトランザクションデータを作成する。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目値がNULL値かどうかをチェックし、
NULL値以外であれば，それらの項目名を1つのアイテムとして連結し
新しいベクトル項目(トランザクション項目とも呼ぶ)として出力する。

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
param['kwd']='a'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
トランザクション項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
ここで指定された項目値(複数項目指定可)をチェックし、トランザクションデータを作成する。
( ``r`` オプションの指定がある時はトランザクションデータから項目名として抜き出す値のリスト)
'''
db['params'].append(param)

param={}
param['kwd']='delim'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
ここで指定した文字をトランザクション項目のアイテム間の区切りとする（省略時はスペース）。
文字列の指定はできない。1バイト文字のみ指定可能。
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
トランザクション型から縦型へデータを変換する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
