# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mvcommon'
db['title']='ベクトル要素の参照選択'
db['related']=[
  ["mvjoin","選択でなくベクトル要素を結合する。"]
]

############################### DOCUMENT
db['doc']='''
ベクトルから、参照データで指定された要素を選択する。
典型的な例を :numref:`mvcommon_input` 〜 :numref:`mvcommon_out3` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mvcommon_input

  no,items
  1,a b c
  2,a d
  3,b f e f
  4,f c d




.. csv-table:: 参照データ
  :header-rows: 1
  :name: mvcommon_ref

  item
  a
  c
  e




.. csv-table:: 基本例
  :header-rows: 1
  :name: mvcommon_out2

  no,items
  1,a c
  2,a
  3,e
  4,c




.. csv-table:: アンマッチアイテムの選択例
  :header-rows: 1
  :name: mvcommon_out3

  no,items
  1,b
  2,d
  3,b f f
  4,f d


``mvcommon`` コマンドは、参照データデータを一旦全てメモリにセットするので、
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
結合キーとなるアイテム集合の項目名( ``i=`` データ上)を指定する。
複数項目指定可能。アイテムはソーティングされている必要はない。
結果の項目名を変更したいときは、:(コロン)に続けて新項目名を指定する。
例) f=数量:置換後の項目名
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
このパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)
'''
db['params'].append(param)

param={}
param['kwd']='K'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']='k=と同一項目名'
param['text']='''
参照データ( ``m=`` )上の結合キーとなるアイテムの項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``vf=`` と ``K=`` の要素がマッチしない要素を選択する。
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
