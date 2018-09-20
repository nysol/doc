# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mrjoin'
db['title']='参照ファイルの範囲条件による結合'
db['related']=[
  ["mchgnum","数値範囲を指定して値を置換/追加する。"],
  ["mjoin","数値範囲ではなく文字列一致による結合の場合はこのコマンドを使う。"],
  ["mnrcommon","結合ではなく選択する場合はこのコマンドを使う。"]
]

############################### DOCUMENT
db['doc']='''
範囲により参照データの項目を結合(join)する。
``r=`` パラメータで指定した項目値が、参照データ上にある範囲条件(項目値以上、次行の項目値未満)にマッチすれば ``f=`` パラメータで指定した項目値を結合する。
より複雑な範囲条件で結合したければ ``mnrjoin`` を使う。
範囲条件数が少なければ ``mchgnum`` の利用を考えるとよい。

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
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
結合する参照データ上の項目名リスト(複数項目指定可)。
省略すると ``K=`` で指定された項目以外の項目を全て結合する。
'''
db['params'].append(param)

param={}
param['kwd']='m'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='標準入力'
param['text']='''
参照データを指定する。
このパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)
'''
db['params'].append(param)

param={}
param['kwd']='rf'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
範囲比較される項目名
入力データ上の項目名を指定する。
ここでここで指定した項目(複数項目指定可)で並べ替えられた後、結合が行われる。
%nが指定されると、数値範囲として解釈し、指定がなければ文字列範囲として解釈する。
ここで指定する項目にNULL値があってはならない。NULL値があった場合の動作は不定である。
'''
db['params'].append(param)

param={}
param['kwd']='R'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
参照データ上の範囲項目名。
省略時は ``r=`` パラメータと同名として扱われる。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
入力データ上の突き合わせる項目名リスト(複数項目指定可)
ここで指定した入力データの項目と ``K=`` パラメータで指定された
'''
db['params'].append(param)

param={}
param['kwd']='K'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='k=と同一項目名'
param['text']='''
参照データ上の突き合わせる項目名リスト(複数項目指定可)
ここで指定した参照データの項目と ``k=`` パラメータで指定された
参照データ上に ``k=`` パラメータで指定した入力データ上の
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
参照データにない入力データをNULL値として出力するフラグ。
'''
db['params'].append(param)

param={}
param['kwd']='lo'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
left open interval
``R=``  パラメータで指定した範囲を左半開区間（より大きい～以下）と解釈する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
