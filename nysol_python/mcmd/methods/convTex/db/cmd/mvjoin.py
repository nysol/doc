# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mvjoin'
db['title']='ベクトル要素の参照結合'
db['related']=[
  ["mvcommon","結合ではなく、要素を選択するだけならこのコマンドを利用する。"]
]

############################### DOCUMENT
db['doc']='''
ベクトル要素をキーにして参照データ上のベクトル型データを結合する。
ベクトル型の項目とは、 :numref:`mvjoin_input` のitems項目のように、
スペースで区切られた複数の文字列を値として持つ項目である。
典型的な例を :numref:`mvjoin_input` 〜 :numref:`mvjoin_out3` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mvjoin_input

  no,items
  1,a b c
  2,a d
  3,b f e f
  4,f c d




.. csv-table:: 参照データ
  :header-rows: 1
  :name: mvjoin_ref

  item,taxo
  a,X
  b,Y
  c,Z
  e,X
  f,Z




.. csv-table:: 基本例
  :header-rows: 1
  :name: mvjoin_out2

  no,items
  1,a b c X Y Z
  2,a d X
  3,b f e f Y Z X Z
  4,f c d Z Z




.. csv-table:: アンマッチ要素の指定例
  :header-rows: 1
  :name: mvjoin_out3

  no,items
  1,a b c X Y Z
  2,a d X *
  3,b f e f Y Z X Z
  4,f c d Z Z *


``mvjoin`` コマンドは、参照データデータを一旦全てメモリにセットするので、
巨大な参照データを指定した場合はメモリを使い果たす可能性があることに注意する。

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
param['kwd']='vf'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
結合キーとなるベクトルの項目名( ``i=`` データ上)を指定する。
複数項目指定可能。ベクトル要素はソーティングされている必要はない。
結果の項目名を変更したいときは、:(コロン)に続けて新項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='A'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``vf=`` で:(コロン)に続けて指定した項目名で、新たな項目が追加される。
なお ``A=True`` オプションを指定した場合、 ``vf=`` パラメータで指定するすべての
項目に新項目名を指定しなければならない。
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
'''
db['params'].append(param)

param={}
param['kwd']='K'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']='k=と同一項目名'
param['text']='''
参照データ( ``m=`` )上の結合キーとなるベクトル要素の項目名を指定する。
並べ変わっている必要はないが、ベクトル要素は単一化されていなければならない。
単一化されていない時の動作は不定である。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
結合するベクトル(要素)項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
``vf=`` と ``K=`` のベクトル要素がマッチしなかった場合に結合する文字列を指定する。
省略した場合、対象のベクトル(要素)の結合は行われない。
'''
db['params'].append(param)

param={}
param['kwd']='delim'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
ベクトル型データの区切り文字を指定する。
'''
db['params'].append(param)

db['comParams']='i,o,delim,assert_diffSize,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
