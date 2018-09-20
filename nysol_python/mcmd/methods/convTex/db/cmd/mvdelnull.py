# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mvdelnull'
db['title']='ベクトルのNULL要素の削除'
db['related']=[
  ["mvnullto","NULL要素を任意の値に置換する。"]
]

############################### DOCUMENT
db['doc']='''
ベクトル要素でNULLの要素を全て削除する。
ベクトル要素がNULLであれば、要素の区切り文字が連続する。
以下に示したベクトルは全てNULLを含む。
ただし、わかりやすさのためにベクトルの末尾に  ``\\n``  を記している。
上から順番に、3番目、1番目、4番目の要素がNULLである。
``a b  c\\n``
``a b\\n``
``a b c \\n``

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
NULL要素を削除する対象となる項目名( ``i=`` データ上)を指定する。
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
