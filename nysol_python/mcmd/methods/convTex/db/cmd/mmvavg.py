# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mmvavg'
db['title']='移動平均の算出'
db['related']=[
  ["mmvstats","平均だけでなく、各種統計量を指定可能。"],
  ["mmvsim","2変量の統計量を計算する。"],
  ["mwindow","動窓のデータを作成するので、そのデータを使えば ``mmvstats`` で計算できない統計量も計算可能。"]
]

############################### DOCUMENT
db['doc']='''
移動平均(moving average)を算出する。
移動平均としては、単純移動平均( :math:`SMA` )、線形荷重移動平均( :math:`WMA` )、指数平滑移動平均( :math:`EMA` )の３種類の移動平均が計算可能である。
ある時 :math:`t` における値を :math:`x_t` で表したとき、 :math:`m` 期の各種移動平均は式(\ref{eq:sma},\ref{eq:wma},\ref{eq:ema})で定義される。
\begin{eqnarray}
SMA_t=\frac{1}{m} \sum_{i=0}^{m-1} x_{t-i}
\label{eq:sma}
\end{eqnarray}
\begin{eqnarray}
WMA_t=\sum_{i=0}^{m-1} \frac{m-i}{S} x_{t-i},\ \ S=\sum_{i=1}^m i
\label{eq:wma}
\end{eqnarray}
\begin{eqnarray}
EMA_t=\alpha x_t + (1-\alpha)EMA_{t-1}
\label{eq:ema}
\end{eqnarray}

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
param['kwd']='s'
param['type']='str'
param['mand']=False
param['cond']=' ``q`` オプションの指定がない場合'
param['default']=''
param['text']='''
ここで指定した項目(複数項目指定可)で並べ替えられた後、移動平均が計算される。
``q`` オプションを指定しないとき、 ``s=`` パラメータは必須。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
ここで指定された項目(複数項目指定可)を単位として集計する。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
移動平均を求める項目名リスト(複数項目指定可)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='t'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
期間数を1以上の整数で指定する。
``exp`` オプション指定時に ``alpha=`` を指定すれば ``t=`` は指定できない。
'''
db['params'].append(param)

param={}
param['kwd']='w'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
線形加重移動平均を求める。
'''
db['params'].append(param)

param={}
param['kwd']='exp'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
指数平滑移動平均を求める。
'''
db['params'].append(param)

param={}
param['kwd']='alpha'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
``exp`` オプションが指定された時の平滑化係数を実数値で与える。
省略時は ``alpha=2/(t=の値+1)`` 。
'''
db['params'].append(param)

param={}
param['kwd']='skip'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
出力を抑制する最初の行数。
デフォルト値:  ``skip=(t=の値-1)`` ,  ``exp`` オプションが指定された場合は ``skip=0``
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
期間内にNULL値が1つでも含まれていると結果もNULL値とする。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
