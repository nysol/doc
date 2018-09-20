# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mcat'
db['title']='併合'
db['related']=[
  ["msep","ちょうど逆の動きをする。"]
]

############################### DOCUMENT
db['doc']='''
``i=`` パラメータで指定した全データのレコードを、指定した順に併合する。
ワイルドカードでデータを指定した場合は、データのアルファベット順に併合される。

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
入力データリストを指定する。
複数のデータをカンマで区切って指定する。ワイルドカードを用いることができる。
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
併合する項目名を指定する。
指定を省略すれば ``i=`` で指定した1つ目のデータの項目名が使われる。
'''
db['params'].append(param)

param={}
param['kwd']='skip_fnf'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``i=`` で指定したデータが存在しなくてもエラー終了しない。
ただし、全データがなければエラーとなる。
'''
db['params'].append(param)

param={}
param['kwd']='nostop'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``nostop``  , ``skip`` , ``force`` の各オプションは、指定の項目名がなかったときの動作を制御するフラグである。
``nostop`` オプションは、指定の項目名がなければnullを出力する。
``nfn`` オプションが同時に指定された場合，項目数が異なればエラー終了する。
'''
db['params'].append(param)

param={}
param['kwd']='skip'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
指定の項目名がなければそのデータは併合しない。
``nfn`` オプションが同時に指定された場合、項目数が異なればそのデータは併合しない。
'''
db['params'].append(param)

param={}
param['kwd']='skip_zero'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``nfn`` オプションを指定していない場合でも0バイトデータでエラーにならないようにする。
'''
db['params'].append(param)

param={}
param['kwd']='flist'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
併合するデータリストをCSVデータとして指定する。flist=fileName:fldNameで指定する。
'''
db['params'].append(param)

param={}
param['kwd']='kv'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
パス名に含めた key-value の文字列を抜き出し項目名とその値としてデータに付加する。
'''
db['params'].append(param)

param={}
param['kwd']='force'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
指定の項目名がなければ，項目番号で強制併合する。
指定の項目番号がなければnullを出力する。
'''
db['params'].append(param)

param={}
param['kwd']='stdin'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
標準入力も併合する。
'''
db['params'].append(param)

param={}
param['kwd']='add_fname'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
併合元のデータを最終項目として追加する。
標準入力は ``/dev/stdin`` という名称になる。
項目名は ``fileName`` 固定なので、入力データに同一の項目名があるとエラーとなる。
'''
db['params'].append(param)

db['comParams']='i,o,add_fname,-stdin,assert_diffSize,assert_nullin,nfn,nfno,x,tmppath,precision'
