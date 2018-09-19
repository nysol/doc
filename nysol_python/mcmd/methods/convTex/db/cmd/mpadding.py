# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mpadding'
db['title']='(行補完) コマンド'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
``k=`` パラメータで指定した項目をキーとして、 ``f=`` パラメータで指定した項目の値が連続するようにレコードを作成する。 ``v=`` パラメータを指定した場合は、 ``k=`` , ``f=`` で指定した以外の項目値を指定した文字列でパディングし、 ``n=True`` オプション指定時は、nullでパディングする。( ``v=`` , ``n=True`` 共に指定がなければ直前の項目値でパディングする)

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
ここで指定された項目をキーとする。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
連続パディング対象項目名
ここで指定された項目の値が連続するようにレコードをパディングする。
数字としてパディングするときは、no\%nのように\%nを指定する。
日付としてパディングするときは\%d、時刻としてパディングするときは\%tを指定する。
降順でパディングしたいときはno\%d\%rのようにrを追加する。
'''
db['params'].append(param)

param={}
param['kwd']='v'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
パディング用文字列指定
k=,f=で指定した以外の項目値を指定した文字列で出力する。
'''
db['params'].append(param)

param={}
param['kwd']='S'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
開始値
f=で指定した項目の値の開始値を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='E'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
終了値
f=で指定した項目の値の終了値を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
パディングにnull値指定
k=,f=で指定した以外の項目値をnullで出力する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,x,tmppath,precision'
