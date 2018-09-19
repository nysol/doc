# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mvcat'
db['title']='ベクトルの併合'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
複数のベクトルを併合して新しいベクトルを生成する。
典型的な例を :numref:`mvcat_input` 〜 :numref:`mvcat_out2` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mvcat_input

  no,items1 items2
  1,a c b
  2,a d a e
  3,b f
  4,e e




.. csv-table:: 基本例
  :header-rows: 1
  :name: mvcat_out1

  no,catItems
  1,a c b
  2,a d a e
  3,b f
  4,e e




.. csv-table:: 併合前のベクトルを残す例
  :header-rows: 1
  :name: mvcat_out2

  no,items1 items2 new
  1,a c b a c b
  2,a d a e a d a e
  3,b f  b f
  4,e e e e



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
併合する複数のベクトル項目名( ``i=`` データ上)を指定する。
項目名にワイルドカードを使うことができる。
'''
db['params'].append(param)

param={}
param['kwd']='a'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
併合後の項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='A'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
新しい項目として追加する。このオプションを指定しなければ、併合元の項目( ``vf=`` )は削除される。
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
