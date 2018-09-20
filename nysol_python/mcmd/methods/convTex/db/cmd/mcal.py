# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mcal'
db['title']='項目間演算'
db['related']=[
  ["msel","演算の結果を用いて行選択するのであればこちらを使う。"]
]

############################### DOCUMENT
db['doc']='''
``c=`` パラメータで指定した計算式で計算をおこない、 ``a=`` パラメータで指定した項目名に出力する。
``mcal`` が出力する項目は、プログラムの単純化のため、例外なく1つに限定している。
計算式の詳細はの「 :doc:`../calsel` 」の節を参照のこと。

**エラーメッセージについて**

``#ERROR# unknown function or operator``

このエラーメッセージが出るということは、関数もしくは演算子の指定に誤りがある。
例えば、以下のような文字列の結合関数catについてのエラーメッセージについて考える。

  .. code-block:: python
    :linenos:
    :caption: cat関数のエラー
    :name: mcal_error

		nm.mcal(c='cat("-",1,2)').run()
		#ERROR# : unknown function or operator: cat_SNN(cat_SN) (kgcal)
 
「cat_SNN」のアンダーバーの前のcatは関数名を示し、その後のSNNは引数の型を示している。
Sは文字列型、Nは数字型、Dは日付型、Tは時刻型、Bは真偽型である。
3つの引数を指定しているので3文字(SNN)となっている。
すなわち、このエラーメッセージは「引数としてSNNをとるcatという関数」
は登録されていないということを意味する。
ここで、エラーメッセージの括弧の中は2文字(SN)となっているが、
それは2番目以降のパラメータが可変個指定可能であるため、
それらの代表として１つだけ表記しているためである。

以下のように2,3番目の引数を文字列型にすればよい。

  .. code-block:: python
    :linenos:
    :caption: cat関数のエラー
    :name: mcal_error2

		nm.mcal(c='cat("-","1","2")').run()
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
param['kwd']='a'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
新たに計算結果の出力として追加される項目の名前を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='c'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
用意された関数を組み合わせて計算する式を指定する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullout,nfn,nfno,x,tmppath,precision'
