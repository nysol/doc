# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mbucket'
db['title']='件数均等化バケット分割'
db['related']=[
  ["mmbucket","多次元のセルで件数均等化分割をする場合はこちらを使う。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` で指定した数値項目を ``n=`` で指定した数の区間に分割する。
区間の計算には2通りの方法があり、一つは、
各区間に属する件数ができるだけ均等になるような区間を計算する
(件数均等化バケット分割と呼ぶ)。
他方は、区間の範囲が均等になるような区間を計算する
(範囲均等化バケット分割と呼ぶ)。
``rng`` オプションを指定すると範囲均等分割となり、指定しなければ件数均等分割となる。
``f=`` に複数の項目を指定した場合は、それぞれの項目ごとにバケット分割を実行する。

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
ここで指定した項目(複数項目指定可)の値に基づいて分割をおこなう。
分割対象の項目名:出力する項目名
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
分割数
``f=`` で指定した項目それぞれの分割数をカンマで区切って指定する。
ただし1つの数字を指定した場合は全ての項目の分割数として扱われる。
'''
db['params'].append(param)

param={}
param['kwd']='F'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='0'
param['text']='''
出力形式
バケットの名前を出力形式。
0:バケット番号のみを表示する。
1:バケットの範囲のみを表示する。
2:バケット番号とバケット範囲の両方を表示する。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
バケット分割を行う単位となる項目(複数項目指定可)名リスト。
'''
db['params'].append(param)

param={}
param['kwd']='O'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
バケット範囲出力データ
``f=`` パラメータで指定した各項目の各バケットの数値範囲を出力するデータ。
'''
db['params'].append(param)

param={}
param['kwd']='rng'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
バケットの範囲均等指定
バケットの範囲が均等になるように分割する。
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
バケットの番号を逆順に出力する。
'''
db['params'].append(param)

param={}
param['kwd']='bufcount'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
バッファのサイズ数を指定する。
'''
db['params'].append(param)

db['comParams']='i,o,bufcount,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
