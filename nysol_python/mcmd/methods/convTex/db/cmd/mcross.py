# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mcross'
db['title']='クロス集計'
db['related']=[
  ["mtra","横展開するイメージは同じだが、 ``mtra`` は1つのベクトル項目として出力する。"]
]

############################### DOCUMENT
db['doc']='''
クロス集計を行う。
``s=`` で指定した項目の値が項目名となるように横に展開され、
``k=`` で指定した値が行idとなり、
``f=`` で指定した項目がセルとして出力される。

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
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
ここで指定された項目の値がセルの値として出力される。
複数項目指定すると、複数行に展開される。
それら複数行を識別するための項目として ``fld`` 項目が出力され、
``f=`` で指定した項目名が値として出力される。
この ``fld`` という項目名を変更したい場合は ``a=`` パラメータを使う。
'''
db['params'].append(param)

param={}
param['kwd']='s'
param['type']='str'
param['mand']=True
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
``f=`` で指定した項目名がデータとして展開される項目名を指定する。
省略した場合は ``fld`` という項目名で出力される。
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
ここで指定した項目を単位に横展開をおこなう。
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
