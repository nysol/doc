# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='marff2csv'
db['title']='arff形式からcsv形式への変換'
db['related']=[
  ["mcsv2arff",""],
  ["\subsection*{参考資料}",""],
  ["\href{http://weka.wikispaces.com/ARFF}{http://weka.wikispaces.com/ARFF}",""]
]

############################### DOCUMENT
db['doc']='''
arff形式(WEKA用のデータフォーマット)のデータからcsv形式のデータへ変換する。
\subsubsection*{arff形式データ}
以下arff形式データのフォーマットを記載する。
``@RELATION       タイトル``
``@ATTRIBUTE      項目名    string(文字列)``
``@ATTRIBUTE      項目名    date(日時 フォーマット:フォーマットは省略可能。``
``省略した場合は、"yyyy-MM-dd'T'HH:mm:ss"）``
``@ATTRIBUTE      数量    numeric(数字)``
``@ATTRIBUTE      商品    {A,B}(カテゴリ型項目)``
``@DATA(実データ)``
``No.1,20081201,1,10,A``
``No.2,20081202,2,20,A``
``No.3,20081203,3,30,A``
``No.4,20081201,4,40,B``
``No.5,20081203,5,50,B``

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

db['comParams']='i,o,assert_nullout,nfn,nfno,x,q,tmppath,precision'
