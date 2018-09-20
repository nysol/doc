# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mnewrand'
db['title']='乱数データの新規生成'
db['related']=[
  ["mnewnumber","連番を生成する。"],
  ["mnewstr","固定文字列を生成する。"]
]

############################### DOCUMENT
db['doc']='''
0.0から1.0の範囲の実数乱数を生成する。
``int`` オプションを指定することで、整数乱数を生成することもできる。
乱数の生成にはメルセンヌ・ツイスター法を利用している
(\href{http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html}{原作者のページ}
, \href{http://www.boost.org/doc/libs/1_54_0/doc/html/boost_random.html}{boostライブラリ})。

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
param['kwd']='a'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
新規に作成するデータの項目名を指定する。
``nfn`` もしくは ``nfno`` オプション指定時は指定の必要はない。
'''
db['params'].append(param)

param={}
param['kwd']='max'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='INT\_MAX'
param['text']='''
乱数の最大値を指定する。
このパラメータを指定するときは ``int`` オプションも指定しなければならない。
'''
db['params'].append(param)

param={}
param['kwd']='min'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='0'
param['text']='''
乱数の最小値を指定する。
このパラメータを指定するときは ``int`` オプションも指定しなければならない。
'''
db['params'].append(param)

param={}
param['kwd']='S'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='現在時刻'
param['text']='''
乱数の種を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='l'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='10'
param['text']='''
行数
新規作成する乱数データの行数を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='int'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
整数乱数を生成する
'''
db['params'].append(param)

db['comParams']='o,nfn,nfno,x,tmppath,precision'
