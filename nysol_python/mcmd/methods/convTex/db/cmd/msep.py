# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='msep'
db['title']='レコードの分割'
db['related']=[
  ["msep2","``msep`` と同じような機能だが、データは連番で出力し、キー項目との対応表を別途データに出力する。"],
  ["mcat","``msep`` で分割したデータをこのコマンドで併合すると元に戻る。"]
]

############################### DOCUMENT
db['doc']='''
``d=`` パラメータで指定したデータのデータに各レコードを出力する。
指定するデータに項目名を埋め込むことができるので、結果としてレコード分割することになる。
埋め込むデータは ``${項目名}`` によって指定する。
例えば、 ``d=./out/${date}.csv`` と指定すれば、カレントディレクトリの下の ``out`` ディレクトリの下に、
``date`` 項目の値別にデータが作成されることになる。
内部的には、埋め込んだ項目の値をキーとして認識し、並べ替えが行われた後レコードが分割される。

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
param['kwd']='d'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
異なるデータデータに分割する項目名を指定する。
ここで指定した文字列をデータとして各レコードが追記されていく。
項目名は ``${項目名}`` によって埋め込む。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
出力する項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='p'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``d=``  パラメータで指定したディレクトリ名が存在しなければ作成する。
'''
db['params'].append(param)

db['comParams']='i,assert_nullin,nfn,nfno,x,q,tmppath,precision'
