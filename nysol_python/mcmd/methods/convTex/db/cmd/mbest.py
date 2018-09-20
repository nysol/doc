# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mbest'
db['title']='指定行の選択'
db['related']=[
  ["msel","``line()`` 関数を使えば、同じようなことができる。"],
  ["muniq","単純にキー項目を単一化したいだけならこれ。"],
  ["mselnum","数値範囲によって行選択ができる。"]
]

############################### DOCUMENT
db['doc']='''
指定した行番号の行を選択する。
行番号は0から始まることに注意する(項目名行は除いて、データ本体の先頭行が0行目)。
行番号は ``fr=`` と ``to=`` (もしくは ``size=`` )で指定する。
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
param['kwd']='s'
param['type']='str'
param['mand']=True
param['cond']=' ``q`` オプションの指定がない場合'
param['default']=''
param['text']='''
ここで指定した項目(複数項目指定可)で並べ替えられた後、指定した行が選択される。
``q`` オプションを指定しないとき、 ``s=`` パラメータは必須。
'''
db['params'].append(param)

param={}
param['kwd']='fr'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='0'
param['text']='''
選択する開始行番号(0以上の整数)
'''
db['params'].append(param)

param={}
param['kwd']='to'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='0'
param['text']='''
選択する終了行番号(0以上の整数)
「 ``fr=`` の値」 :math:`\le` 「 ``to=`` の値」でなければならない。
'''
db['params'].append(param)

param={}
param['kwd']='size'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='1'
param['text']='''
選択する行数
``to=`` と ``size=`` の両方を同時に指定することはできない。
'''
db['params'].append(param)

param={}
param['kwd']='R'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
行番号範囲リスト(複数項目指定可)【必須】*以前のバージョンで使用されていた範囲指定の方法
ここで指定した行番号の行が選択される。
\_(アンダーバー)で範囲指定できる。
範囲指定の際にはMIN(開始行以降),MAX(最終行まで)を使用できる。
※One Point：事前に目的とする行選択が行いやすいように並べ替えておくとよい。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
指定列の項目(複数項目指定可)が同じ値の行ごとに、 ``fr=`` , ``to=`` , ``size=`` で指定した行番号の行を選択する。
``x`` オプションもしくは ``nfn`` オプション使用時は、項目番号(0〜)で指定可能。
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='出力しない'
param['text']='''
不一致データ出力データ
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
``fr=,to=(size=)`` パラメータで指定した行番号以外の行を選択する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,nfn,nfno,x,q,tmppath,precision'
