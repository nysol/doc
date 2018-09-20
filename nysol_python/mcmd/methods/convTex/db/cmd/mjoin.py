# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mjoin'
db['title']='参照ファイルの項目結合'
db['related']=[
  ["mnjoin","参照データのキーに重複がある場合は ``mnjoin`` を使う。"],
  ["mpaste","行番号による結合を行う。"],
  ["mcommon","結合でなく単に選択するだけなら ``mcommon`` を使えばよい。"]
]

############################### DOCUMENT
db['doc']='''
``k=`` パラメータで指定した入力データの項目値と参照データの項目値を比較し、
同じ値を持つ ``f=`` パラメータで指定した参照データの項目値を結合する。
参照データのキー項目は単一化されている必要がある。
参照データに同じキー項目の値が複数ある場合は、 :doc:`mnjoin <mnjoin>` を利用すればよい。
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
ここで指定した入力データの項目と ``K=`` パラメータで指定された
参照データの項目が同じ行の項目結合が行われる。
NULL値は，参照データの ``K=`` で指定した項目のどの値にもマッチしない値として扱われる。
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
ここで指定した参照データの項目と ``k=`` パラメータで指定された入力データの項目が同じ行の項目結合が行われる。
NULL値は，入力データの ``k=`` で指定した項目のどの値にもマッチしない値として扱われる。
参照データ上に ``k=`` パラメータで指定した入力データ上の
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

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
