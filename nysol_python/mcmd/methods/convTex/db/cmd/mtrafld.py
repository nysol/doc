# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mtrafld'
db['title']='クロス表をトランザクション項目に変換'
db['related']=[
  ["mvsort","トランザクションデータはベクトル型データを処理する一連の処理コマンド( ``mv`` から始まる)によって加工できる。"],
  ["mcross","トランザクションデータとしてではなく、個々のアイテムを独立した項目として出力し、その出現件数を出力する。"],
  ["mtra","項目の値をアイテムとしてトランザクションデータを作成する。"],
  ["mtraflg","項目名をアイテムとしてトランザクションデータを作成する。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` で指定した項目値とその値のペアのアイテムを作成し、
それらのアイテムを連結し新しいベクトル項目(トランザクション項目とも呼ぶ)として出力する。

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
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
項目名リスト(複数項目指定可)【 ``r=True`` 指定時必須、それ以外は任意】
ここで指定された項目名と値とを連結したアイテムを作成し
トランザクション項目として出力される。
``r=True`` オプションの指定がある時は
トランザクションデータから抜き出す項目名を指定する。
``r=True`` オプションが指定されたとき，このパラメータは省略可能である。
省略すると、全ての項目名と値ペアを処理対象とする。
ただし、 ``f=`` パラメータを省略すると標準入力(パイプ入力)は利用できない。
'''
db['params'].append(param)

param={}
param['kwd']='delim'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
トランザクション項目のアイテムを区切る文字を指定する(省略時はスペース)。
'''
db['params'].append(param)

param={}
param['kwd']='delim2'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
項目名と値ペアとを区切る文字を指定する(省略時は=)。
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
トランザクション項目をクロス表に変換する。
'''
db['params'].append(param)

param={}
param['kwd']='valOnly'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
このオプションが指定されると、アイテムとして「項目名=」は出力しない。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
