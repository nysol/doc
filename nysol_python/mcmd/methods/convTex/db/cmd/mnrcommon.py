# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mnrcommon'
db['title']='参照ファイルの複数範囲条件による行撰択'
db['related']=[
  ["mcommon","範囲でなく文字列マッチで選択したい場合はこのコマンドを使う。"],
  ["mnrjoin","選択ではなく参照データの項目を結合する。"]
]

############################### DOCUMENT
db['doc']='''
参照データの範囲条件にマッチする入力データの行を選択する。
``k=`` パラメータで指定した入力データの項目値と ``K=`` パラメータで指定した参照データの項目値が同じ行について、
``r=`` でパラメータで指定した項目値が ``R=`` パラメータで指定した2項目の値の範囲条件(項目1以上項目2未満)にマッチすれば選択する。
数値として処理したい場合は ``r=`` パラメータの項目名のあとに ``%n`` をつけること。

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
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
入力データ上の突き合わせる項目名リスト(複数項目指定可)を指定する。
ここで指定した入力データの項目と ``K=`` パラメータで指定された参照データの項目が同じ行の項目結合が行われる。
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
参照データ上の範囲項目名(start,end)を指定する。
第一項目のNULL値は無限小，第二項目のNULL値は無限大として扱われる。
'''
db['params'].append(param)

param={}
param['kwd']='fr'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
範囲比較される入力データ上の項目名を指定する。
ここで指定した参照データの項目と ``k=`` パラメータで指定された入力データの項目が同じ行が選択される。
数値として処理したい場合は ``r=`` パラメータの項目名のあとに\%nをつける。
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
param['kwd']='u'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='出力しない'
param['text']='''
指定の条件に一致しない行を出力するデータ。
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
``R=`` パラメータで指定した行番号以外の行を選択する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,nfn,nfno,x,q,tmppath,precision'
