# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mduprec'
db['title']='レコードの複写'
db['related']=[
  ["mcount","``mduprec`` と逆の動きをする。"],
  ["mwindow","一定数のレコードをずらしながら複写する。"]
]

############################### DOCUMENT
db['doc']='''
各レコードを複写する。
複写する行数は ``n=`` で固定値を与えるか、
もしくは ``f=`` で指定した項目の値により与える。

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
param['default']=''
param['text']='''
複写行数をもつ項目名
ここで指定した項目の値の数分、その行を複写する。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
複写行数の指定
ここで指定した値の数分、行を複写する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullin,nfn,nfno,x,tmppath,precision'
