# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mhashsum'
db['title']='ハッシュ法による項目値の合計'
db['related']=[
  ["msum","同じ機能をもつコマンドだが、内部的にキー項目の並べ替えを行う。"],
  ["mhashavg","同じくハッシュ法を用いた平均計算。"]
]

############################### DOCUMENT
db['doc']='''
hash法を使って ``k=`` パラメータで指定した項目を単位にして、 ``f=`` パラメータで指定した項目値を合計する。
:doc:`msum` との違いは、キー項目の並べ替えが必要ないため、その分処理速度が速い。
ただし、キーのサイズ(キー項目のとる値の種類数)が多い場合は処理速度が遅くなる。
msumとmhashsumのどちらを利用するかはデータの内容からユーザーが判断する(後半に示す「ベンチマーク」参照)。

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
ここで指定された項目(複数項目指定可)が合計される。
:(コロン）で新項目名を指定可能。例）f=数量:数量合計
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
ここで指定された項目(複数項目指定可)をキーとして集計する。
'''
db['params'].append(param)

param={}
param['kwd']='hs'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
ハッシュサイズ
処理対象データのキーサイズから，ユーザが消費メモリ量と速度を判断して指定する。指定する値としては素数がよい。
キーサイズが大きいデータに対してハッシュサイズが十分な大きさでなければ処理速度が遅くなる。
ハッシュサイズが十分に大きいと処理速度は速いが、
その分多くのメモリが必要になる(後半に示す「ベンチマーク」参照)。
必要なメモリ量の目安: K*(24+F*16) byte, K:キーのサイズ, F:f=で指定した項目数
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
NULL値が1つでも含まれていると結果もNULL値とする。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
