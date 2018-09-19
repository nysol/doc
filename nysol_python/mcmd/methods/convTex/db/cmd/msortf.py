# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='msortf'
db['title']='レコードの並べ換え'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目を基準にして、レコードを並べ換える。\\
ソーティングアルゴリズムはquick sortを利用しており、
安定ソート(キーの値が同じ行については元の順序を保存する)にはならないことに注意する。\\
出力CSVの項目名の後ろには、並び順情報として ``%`` で始まる文字列が付加される。
書式は ``%優先順位[並び順]`` で、
詳細は以下、 ``f=`` パラメータを参照のこと。

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
レコードを並べ換える基準となる項目名リストを指定する。
並び順は、数値/文字列、昇順/降順の組み合せで4通り指定できる。
指定方法は ``%`` に続けて ``n`` と ``r`` を以下の通り組み合わせる。
文字列昇順: ``項目名`` ( ``%`` 指定なし)、文字列逆順: ``f=項目名%r`` 、数値昇順: ``f=項目名%n`` 、数値降順: ``f=項目名%nr`` 。
'''
db['params'].append(param)

param={}
param['kwd']='noflg'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
出力CSVのヘッダーにソーティングの印( ``%0,%0n`` など)を付けない。
'''
db['params'].append(param)

param={}
param['kwd']='pways'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
同時併合データ数([2-100]:デフォルト32)【任意】
分割ソートされた複数のデータを同時に何個併合するかを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='blocks'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
バッファブロック数([1-1000]:デフォルト10)【任意】
メモリ内でソートする際のメモリサイズ上限をブロックサイズで指定する。
1ブロックは入力バッファサイズ×4で、デフォルトは4MB。
'''
db['params'].append(param)

param={}
param['kwd']='maxlines'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
メモリソートレコード件数上限([100-1000万]:デフォルト50万)【任意】
メモリ内でソートする際の件数の上限を指定する。
データの一行あたりの平均サイズに応じて、
'''
db['params'].append(param)

param={}
param['kwd']='threadCnt'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
メモリ内でソートを実行するthread数 ([1-50]:デフォルト8)【任意】
分割ソートする際に、マルチスレッドの機能を用いて同時にソートする数を指定する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,nfn,nfno,x,tmpPath,precision'
