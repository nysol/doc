# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mnjoin'
db['title']='参照ファイル項目の自然結合'
db['related']=[
  ["mjoin","参照データのキーが単一化されているのであれば ``mjoin`` を使うと若干高速。"],
  ["mproduct","結合キー関係なく全行の組み合せで結合する。1行だけからなる参照データを入力データ全行に結合する目的で利用することが多い。"]
]

############################### DOCUMENT
db['doc']='''
``k=`` パラメータで指定した入力データの項目値と参照データの項目値を比較し、
同じ値の場合 ``m=`` パラメータで指定した参照データにある
``f=`` パラメータで指定した項目値を自然結合する。
``mjoin`` コマンドとの違いは、参照データ上のキー項目に重複があってもよい点である。
あるキー値について、入力データ上に :math:`n` 件、参照データ上に :math:`m` 件のレコードがあった場合、
:math:`n\times m` 件のレコードが出力されることになる。
また、 ``f=`` を省略すると、参照データのキー項目以外全ての項目を結合する。

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
param['kwd']='k'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
入力データ上の突き合わせる項目名リストを指定する。
ここで指定した入力データの項目と ``K=`` パラメータで指定された
参照データの項目が同じ行の項目結合が行われる。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='全項目'
param['text']='''
結合する参照データ上の項目名リストを指定する。
省略するとキー項目を除いた全ての項目が結合される。
'''
db['params'].append(param)

param={}
param['kwd']='m'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='標準入力'
param['text']='''
参照データを指定する。
このパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)
'''
db['params'].append(param)

param={}
param['kwd']='K'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='k=と同一項目名'
param['text']='''
参照データ上の突き合わせる項目名リスト
ここで指定した参照データの項目と ``k=`` パラメータで指定された
参照データ上に ``k=`` パラメータで指定した入力データ上の
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
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
参照データにない入力データをNULL値として出力するフラグ。
'''
db['params'].append(param)

param={}
param['kwd']='N'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
入力データにない参照データをNULL値として出力するフラグ。
'''
db['params'].append(param)

db['comParams']='i,o,bufcount,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
