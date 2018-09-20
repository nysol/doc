# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mnrjoin'
db['title']='参照ファイルの複数範囲条件による自然結合'
db['related']=[
  ["mrjoin","参照データの結合キー( ``K=`` 項目)に重複がなければ ``mrjoin`` を使う。"]
]

############################### DOCUMENT
db['doc']='''
範囲により参照データの項目を結合(join)する。
``r=`` パラメータで指定した項目値が、 ``m=`` パラメータで指定した参照データの
``R=`` パラメータで指定した2項目の値の範囲条件(項目1以上項目2未満)に
マッチすれば ``f=`` パラメータの項目を結合する。
マッチする行が複数あれば、それらの行全てが出力され、ちょうど自然結合のような動きをする。
範囲比較される値は、デフォルトで文字列と見なされる。
数値として処理したい場合は ``r=`` パラメータの項目名のあとに\%nをつける。

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
param['mand']=False
param['cond']=''
param['default']='全項目'
param['text']='''
結合する参照データ上の項目名リスト(複数項目指定可)を指定する。
省略するとK=で指定された項目以外の項目を全て結合する。
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
param['kwd']='R'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
範囲項目名リスト(二項目限定)
参照データ上の範囲項目名(start,end)を指定する。
第一項目のNULL値は無限小，第二項目のNULL値は無限大として扱われる。
'''
db['params'].append(param)

param={}
param['kwd']='rf'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
範囲比較される項目名[\%{n}]
入力データ上の項目名を指定する。
数値として処理したい場合は ``rf=`` パラメータの項目名のあとに\%nをつける。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
入力データ上の突き合わせる項目名リスト(複数項目指定可)
ここで指定した入力データの項目と ``K=`` パラメータで指定された参照データの項目が同じ行の項目結合が行われる。
'''
db['params'].append(param)

param={}
param['kwd']='K'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='k=と同一項目名'
param['text']='''
参照データ上の突き合わせる項目名リスト(複数項目指定可)
ここで指定した参照データの項目と ``k=`` パラメータで指定された入力データの項目が同じ行の項目結合が行われる。
参照データ上に ``k=`` パラメータで指定した入力データ上の項目と同名の項目が存在する場合は指定する必要はない。
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
