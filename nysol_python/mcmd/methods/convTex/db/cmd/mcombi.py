# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mcombi'
db['title']='組合せ計算'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目について、
``n=`` パラメータで指定した数の組み合せを求め、
``a=`` パラメータで指定した項目名で出力する。
``p`` オプションを指定することで順列として出力することも可能である。

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
新たに追加される項目の名前を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
組合せを求める項目名リスト（複数項目指定可）を指定する。
ここで指定した項目の値の全組合せを出力する。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
組合せの数を指定する。
組み合わせ数を大きくすると、出力レコードが爆発的に大きくなることに注意する。
'''
db['params'].append(param)

param={}
param['kwd']='s'
param['type']='str'
param['mand']=False
param['cond']=' ``q`` オプションの指定がない場合'
param['default']=''
param['text']='''
ここで指定した項目(複数項目指定可)で並べ替えられた後、 ``f=`` で指定した項目の組み合わせを求める。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
キー項目名リスト(複数項目指定可)
組合せを求める単位となる項目名リスト。
'''
db['params'].append(param)

param={}
param['kwd']='p'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
組合せでなく順列を求める。
'''
db['params'].append(param)

param={}
param['kwd']='dup'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
同一の値の組み合せも出力する
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullin,nfn,nfno,x,q,tmppath,precision'
