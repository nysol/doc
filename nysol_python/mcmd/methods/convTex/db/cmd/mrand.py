# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mrand'
db['title']='擬似乱数'
db['related']=[
  ["mselrand","ランダムに行を選択する。"],
  ["mnewrand","入力データなしに、乱数データを新たに生成する。"]
]

############################### DOCUMENT
db['doc']='''
0.0から1.0の範囲の実数の擬似乱数、もしくは範囲指定による整数の擬似乱数を生成し、 ``a=`` パラメータで指定した項目名で出力する。
乱数の生成にはメルセンヌ・ツイスター法を利用している
(\href{http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html}{原作者のページ}
, \href{http://www.boost.org/doc/libs/1_54_0/doc/html/boost_random.html}{boostライブラリ})。

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
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
指定したキー項目について、同じキー値には同じ乱数値が振られる。
'''
db['params'].append(param)

param={}
param['kwd']='a'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
新たに追加される項目の名前を指定する。【但し、-nfn,-nfnoオプション指定時は必要なし】
'''
db['params'].append(param)

param={}
param['kwd']='max'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='INT\_MAX'
param['text']='''
乱数の最大値
0〜 :math:`2^{32}` (約21億)の範囲の整数が指定可能
このパラメータを指定するときは ``int=True`` も指定しなければならない。
'''
db['params'].append(param)

param={}
param['kwd']='min'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='0'
param['text']='''
整数乱数の最小値
0〜 :math:`2^{32}` (約21億)の範囲の整数が指定可能
このパラメータを指定するときは ``int=True`` も指定しなければならない。
'''
db['params'].append(param)

param={}
param['kwd']='S'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='現在時刻'
param['text']='''
乱数の種
同じ乱数の種を指定すれば、同じ乱数系列となる。
``S=`` を指定しなければ、時刻(ミリ(1/1000秒単位)に応じた異なる乱数の種が利用される。
指定可能な乱数の種(-2147483648〜2147483647)
'''
db['params'].append(param)

param={}
param['kwd']='int'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
整数乱数を生成
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,nfn,nfno,x,q,tmppath,precision'
