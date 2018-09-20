# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='m2cross'
db['title']='1対Nのクロス集計'
db['related']=[
  ["mcross","イメージは同じだが、 ``mcross`` はN対Nクロス集計として出力する。\\"]
]

############################### DOCUMENT
db['doc']='''
1対Nのクロス集計を行う。
``s=`` を指定した場合には項目の値が項目名となるように横に展開され、
``f=`` で指定した項目がセルとして出力される。
``a=`` を指定した場合(2項目指定)には
指定した値が項目名となり、
１項目に ``f=`` で指定した項目名が、
２項目に ``f=`` で指定した項目値がそれぞれ縦展開される
``k=`` が指定されていた場合には、
指定した値が行idとなり、id単位で展開される。

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
param['kwd']='fixfld'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
横に展開する際、データがない場合に追加する項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
ここで指定された項目の値がセルの値として出力される。
a=を使用するときのみ複数項目指定可。
'''
db['params'].append(param)

param={}
param['kwd']='s'
param['type']='str'
param['mand']=False
param['cond']=' ``q`` オプションの指定がない場合'
param['default']=''
param['text']='''
列項目名に展開する項目を指定する。
ここで指定された項目の値が項目名として出力される。
'''
db['params'].append(param)

param={}
param['kwd']='a'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
２項目指定する。
１項目目に ``f=`` で指定した項目名がデータとして展開される項目名を指定する。
２項目目に ``f=`` で指定した項目値の項目名を指定する
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
キー項目名リスト
ここで指定した項目を単位に展開をおこなう。
'''
db['params'].append(param)

param={}
param['kwd']='v'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
NULL値置換文字列
NULL値があった場合、 ``v=`` パラメータで指定する置換文字列により、項目の値を置換する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
