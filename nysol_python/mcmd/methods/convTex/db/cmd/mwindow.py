# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mwindow'
db['title']='スライド窓の生成'
db['related']=[
  ["mmvavg","移動窓の平均(移動平均)に特化した計算コマンド。"],
  ["mmvstats","移動窓の各種統計量を計算する。"]
]

############################### DOCUMENT
db['doc']='''
複数行をずらしながら複製していく。
移動平均の計算など、時系列データにおいて一定幅の窓を設定し、
その窓をずらしながらその窓を単位に何らかの処理(例えば平均)をする目的に利用する。
このような窓をスライド窓(sliding window)と呼ぶ。
典型的な例を :numref:`mwindow_input` 〜 :numref:`mwindow_out2` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mwindow_input

  date,val
  4/6,1
  4/7,2
  4/8,3
  4/9,4




.. csv-table:: wk=date:win t=2
  :header-rows: 1
  :name: mwindow_out1

  win,date,val
  4/7,4/6,1
  4/7,4/7,2
  4/8,4/7,2
  4/8,4/8,3
  4/9,4/8,3
  4/9,4/9,4




.. csv-table:: wk=date:win t=2 -r
  :header-rows: 1
  :name: mwindow_out2

  win,date,val
  4/6,4/6,1
  4/6,4/7,2
  4/7,4/7,2
  4/7,4/8,3
  4/8,4/8,3
  4/8,4/9,4


:numref:`mwindow_input` に示される入力データは日別の集計値が4日分示されており、スーパーの売上推移や株価推移と考えればよい。
この入力データについて、2日間を窓サイズとして移動平均を計算することを考える。
入力データに示される日付4/6〜4/9についてサイズ2の窓を作成すると
[(4/6,1),(4/7,2)], [(4/7,2),(4/8,3)], [(4/8,3),(4/9,4)]の3つの窓が作成される。
ここで`[]'は一つの窓を示し、`()'は行を示すものとする。
そしてこれらの窓のユニークキー(以下「窓キー」と呼ぶ)として、
各窓の日付の最大値( ``wk=`` で指定した項目の最終行の値)をwinという項目名で出力する( :numref:`mwindow_out1` )。
窓キーを各窓の最小値(先頭行)とするには ``r=True`` オプションを用いればよい( :numref:`mwindow_out2` )。
あとは、出力結果( :numref:`mwindow_out1` )に対して ``mavg`` を実行することで移動平均が計算される。
ちなみに ``mmvavg`` コマンドは、上述の一連の処理( ``mwindow`` + ``mavg`` )と同様の処理を行うが、 ``mmvavg`` の方が高速である(約3.5倍速:200MB,1000万件データで窓サイズを10で実験した結果)。

'''

############################### PARAMETERS
db['params']=[]

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
param['kwd']='wk'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
出力データにおいて、窓をユニークに識別する値となる入力データ上の項目を指定する。
ここで指定した項目で並べ替えられたのちスライド窓を生成していくが、
降順で並べ替えるときは\%r、数値として並べ替えるときは\%nと追加する。
数値の降順で並べ替えるときは\%nrと追加すればよい。
またコロンに続いて窓キーの項目名を指定しなければならない。複数項目を指定することもできる。
'''
db['params'].append(param)

param={}
param['kwd']='t'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
窓のサイズ(行数)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
ここで指定された項目の値を単位に窓の生成を行う。
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
窓における基準行を先頭行とする。指定がなければ最終行となる。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
窓のサイズが ``t=`` で指定した行数に満たなくても出力する。
'''
db['params'].append(param)

param={}
param['kwd']='i'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='標準入力'
param['text']='''
入力データ
'''
db['params'].append(param)

param={}
param['kwd']='nfn'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
入力データの1行目を項目名行とみなさない。
'''
db['params'].append(param)

db['comParams']='assert_diffSize,assert_nullkey,nfn,nfno,x,q,tmppath,precision'
