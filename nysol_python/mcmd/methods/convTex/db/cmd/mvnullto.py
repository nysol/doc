# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mvnullto'
db['title']='ベクトル要素のNULL置換'
db['related']=[
  ["mvdelnull","NULL要素を削除する。"]
]

############################### DOCUMENT
db['doc']='''
ベクトル要素でNULLの要素を任意の値に置換する。
ベクトル要素がNULLであれば、要素の区切り文字が連続する。
以下に示したベクトルは全てNULLを含む。
ただし、わかりやすさのためにベクトルの末尾に ```\n'`` を記している。
上から順番に、3番目、1番目、4番目の要素がNULLである。
``a b  c\n``
``a b\n``
``a b c \n``

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
param['kwd']='vf'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
NULL置換の対象となる項目名( ``i=`` データ上)を指定する。
複数項目指定可能。
結果の項目名を変更したいときは、:(コロン)に続けて新項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='A'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``vf=`` で:(コロン)に続けて指定した項目名で、新たな項目が追加される。
なお ``A`` オプションを指定した場合、 ``vf=`` パラメータで指定するすべての
項目に新項目名を指定しなければならない。
'''
db['params'].append(param)

param={}
param['kwd']='v'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
置換文字列を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='p'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
直前の要素で置換する。v=と同時に指定はできない。
'''
db['params'].append(param)

param={}
param['kwd']='O'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
NULL値以外の要素を全て、ここで指定した文字列に置換する。
指定しなければNULL値以外は置換しない。
'''
db['params'].append(param)

param={}
param['kwd']='delim'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
ベクトル型データの区切り文字を指定する。
'''
db['params'].append(param)

db['comParams']='i,o,delim,assert_diffSize,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
