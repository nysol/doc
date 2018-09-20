# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mselrand'
db['title']='ランダムに行を選択'
db['related']=[
  ["msel","正規乱数も使える。"],
  ["mrand","ランダム選択でなく、乱数項目を付け加える。"]
]

############################### DOCUMENT
db['doc']='''
``c=`` パラメータもしくは ``p=`` パラメータで指定した行数をランダムに選択する(非復元抽出)。
``k=`` を指定した場合、同一キーの行から指定の行数をランダムに選択し、
また同時に ``B`` オプションを指定すると、キー単位で選択する。
乱数の生成にはメルセンヌ・ツイスター法を利用している

* 原作者のページ: http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html
* boostライブラリ: http://www.boost.org/doc/libs/1_54_0/doc/html/boost_random.html

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
param['kwd']='c'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
各キーの値毎に選択する行数を指定する。
``p=`` パラメータを指定しない場合の指定は必ず指定する必要がある。
'''
db['params'].append(param)

param={}
param['kwd']='p'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
各キーの値毎に選択する割合をパーセントで指定する。
``c=`` パラメータを指定しない場合の指定は必ず指定する必要がある。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
指定する項目（複数項目指定可）の値が同じ行から、一定行数ランダムに選択する。
'''
db['params'].append(param)

param={}
param['kwd']='S'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
同じ乱数の種は同じシーケンスの乱数をふる。
指定しない場合は、時刻に応じた異なる乱数の種が利用される。
指定可能な乱数の種(-2147483648〜2147483647)
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='出力しない'
param['text']='''
指定の条件に一致しない行を出力するデータを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='B'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
キー単位選択
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,nfn,nfno,x,q,tmppath,precision'
