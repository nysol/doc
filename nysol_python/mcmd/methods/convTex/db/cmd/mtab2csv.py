# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mtab2csv'
db['title']='TSVからCSVデータへの変換'
db['related']=[
  ["mxml2csv",""],
  ["msplit",""]
]

############################### DOCUMENT
db['doc']='''
タブ区切りデータをCSVデータへ変換する。
``d=`` で区切り文字を指定することで、タブ以外の区切り文字のテキストデータも
変換することが可能である。
変換後の項目数に違いある場合には、その直前行まで出力され、
その後エラー終了する。

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
param['kwd']='d'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
区切り文字の指定(１バイト文字のみ指定可)。
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
改行コード(CR:  ``\\r``  )を取り除く。
MCMDが扱うCSVは改行コードがLF(  ``\\n``  )固定であるため、
Windowsのテキスト改行CR+LF(  ``\\r\\n``  )やMacのテキスト改行CR(  ``\\r``  )があれば、
単なる文字列として扱ってしまい、変換後に不具合が生じる。
この問題を回避するためのオプションである。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,nfn,nfno,x,tmppath,precision'
