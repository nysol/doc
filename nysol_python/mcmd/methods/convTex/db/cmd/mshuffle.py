# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mshuffle'
db['title']='レコード分割'
db['related']=[
  ["msep","項目値によるレコードの分割"]
]

############################### DOCUMENT
db['doc']='''
``f=`` で指定した項目のhash値に従って指定した数のデータに入力データを分割する。
分割数(hashサイズ)を :math:`n` とすると、f=で指定した「項目の値」 :math:`v` のhash値は
:math:`n` の剰余( :math:`v` \ mod\  :math:`n` )として計算される。
「項目の値」は、データを文字列として考え、バイト単位の文字コードの合計値として計算される。
``f=`` を指定しなかった場合は、「項目の値」として行番号が用いられる。
そして、各行は、得られたhash値を名前に持ったデータに出力される。
以上の方法により、同じ項目データを持つ行は全て同一のデータに出力されることが保証される。
また、 ``v=`` で重みを指定することで、分割される各データに複数のhash値を割り当てることもできる。
``n=3,v=2,1,3`` と指定すれば、hashサイズを重みの合計 :math:`2+1+3=6` とし、
2つのhash値(0,1)を分割データ0に、1つのhash値(2)を分割データ1に、
そして3つのhash値(3,4,5)を分割データ2に出力する。
重みはhash値の割当数の重みであり、出力行数の重みではないことに注意する。

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
出力するデータの接頭辞を指定する
ここで指定した値＋連番(hash値)が実際に出力されるデータになる
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
分割単位となるキーを指定する
ここで指定した項目値が等しいものは同じデータに出力される
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
分割するデータ数を指定する
'''
db['params'].append(param)

param={}
param['kwd']='v'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
分割するデータごとにデータ量の重みを指定する
'''
db['params'].append(param)

db['comParams']='i,nfn,nfno,x,tmpPath,precision'
