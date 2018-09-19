# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mnumber'
db['title']='連番'
db['related']=[
  ["mnewnumber","新たに連番データを生成する場合に使う。"],
  ["mbest","行番号による選択であれば、 ``mnumber`` を使わずともこのコマンドで。"]
]

############################### DOCUMENT
db['doc']='''
数字連番もしくはアルファベット連番(A,B,...,Z,AA,AB,...,AZ,BA,BB,...,ZZ,AAA,AAB,...)ををふり、 ``a=`` パラメータで指定した項目名で出力する。

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
param['kwd']='a'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
新たに追加される項目の名前を指定する。【但し、-nfn,-nfnoオプション指定時は必要なし】
'''
db['params'].append(param)

param={}
param['kwd']='e'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
同Rankの処理方法
同一キー同一ソート項目値への処理方法を指定する。
指定しない場合は、デフォルトは ``e=seq`` である。
``seq:`` 同Rankの場合は各行に連番を振るが、その順序は不定である。
``same:`` 同Rankの場合は同じNoもしくはアルファベットを付け加える。
``skip:`` 同Rankの場合は同じNoを振り、
次のNoはスキップするようにNoもしくはアルファベット連番を付け加える。
(注意) ``e={same/skip}`` を指定する場合は、 ``s=`` パラメータを同時に指定しなければならない。
'''
db['params'].append(param)

param={}
param['kwd']='I'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
連番の間隔を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
連番もしくは連文字をふる単位となる項目名リスト(複数項目指定可)を指定する。【 :doc:`集計キーブレイク処理` 】
(注意）指定する場合は事前に ``k=`` パラメータで指定する連番、
もしくは連文字をふる単位となる項目順に並べ替えておく必要がある。
'''
db['params'].append(param)

param={}
param['kwd']='s'
param['type']='str'
param['mand']=False
param['cond']=' ``q=True`` の指定がない場合'
param['default']=''
param['text']='''
ここで指定した項目(複数項目指定可)で並べ替えられた後、連番が追加される。
``B=True`` オプション指定時以外は必須。
'''
db['params'].append(param)

param={}
param['kwd']='S'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
開始No
連番の開始Noを指定する。
大文字のアルファベットが指定された場合はアルファベット連番となる。
ただし、アルファベット連番の場合、間隔( ``I=`` )に負の値は指定できない。
'''
db['params'].append(param)

param={}
param['kwd']='B'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
キー毎に連番もしくはアルファベット連番をふる。
あるキー内では全行同じNoもしくはアルファベットがふられる。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,nfn,nfno,x,q,tmppath,precision'
