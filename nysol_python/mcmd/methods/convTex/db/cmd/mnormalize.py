# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mnormalize'
db['title']='基準化'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目を、 ``c=`` パラメータで指定した基準化の方法で基準化する。\\

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
param['kwd']='c'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
以下に示す基準化の方法のいずれかを指定する。
``z``  : z得点 :  :math:`z_i=(x_i-m)/u`  ( :math:`x_i` :  :math:`i` 番目のデータ,  :math:`m`  :算術平均,  :math:`u`  :標準偏差)
``Z``  : 偏差値 :  :math:`Z_i=50+10\times z_i` 
``range``  : 最小値を0,最大値を1に線形変換  :math:`r_i=(x_i-\min_x)/(\max_x-\min_x)` 
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
ここで指定された項目が基準化される。
:(コロン）で新項目名を指定する必要がある。例） ``f=`` 数量:数量基準値
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
ここで指定された項目を単位に基準化を行う。
'''
db['params'].append(param)

param={}
param['kwd']='bufcount'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
バッファのサイズ数を指定する。
'''
db['params'].append(param)

db['comParams']='i,o,bufcount,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
