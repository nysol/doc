# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mmbucket'
db['title']='多次元均等化バケット分割'
db['related']=[
  ["mbucket","複数項目指定しても、それぞれの項目で1次元バケット分割を実行する。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` で指定した複数の数値項目を次元とした件数均等化バケット分割を行う。
例えば、 ``f=a,b,c`` そして ``n=5`` と指定すると、
:doc:`mbucket` コマンドと同様に、項目 ``a,b,c`` それぞれを5つの区間に分割するが、
``mmbucket`` では、項目 ``a,b,c`` の3次元空間における各バケット(バケット数は :math:`5^3=125` 個になる)に
属する件数ができるだけ均等になるような区間を計算する

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
ここで指定した項目(複数項目指定可)の値を分割する。
複数指定すれば、その数の次元に基づく均等化バケット分割を行う。
1項目のみ指定すれば ``mbucket`` と同じ結果になる。
``x,-nfn=True`` オプション使用時は、項目番号(0〜)で指定可能。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
``f=`` で指定した項目数と同じ個数分指定する。
ただし1つの数字を指定した場合、 ``f=`` で指定した全ての項目に、同じ分割数が適用される。
'''
db['params'].append(param)

param={}
param['kwd']='F'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='1'
param['text']='''
出力形式を指定する。
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
バケット分割を行う単位となる項目名リスト(複数項目指定可)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='O'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
``f=`` パラメータで指定した各項目の各バケットの数値範囲を出力するデータを指定する。
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

param={}
param['kwd']='ms'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
各項目を順次バケット分割していく時の開始項目を変えることで複数回のバケット分割をトライし、
よりよい解を求める。詳細は、以下の「アルゴリズムの概要」を参照のこと。
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
バケット番号を逆順に出力する。
'''
db['params'].append(param)

db['comParams']='i,o,bufcount,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
