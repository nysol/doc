# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mvdelim'
db['title']='ベクトル要素の区切り文字変更'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
ベクトル型の要素を区切る文字列を変更する。
ただし、区切り文字に空文字を指定すれば区切り文字を削除することになる。
典型的な例を :numref:`mvdelim_input` 〜 :numref:`mvdelim_out4` に示す。
カンマも指定することはできるが、
ダブルクォーテーションで括られ 一つの項目となる ( :numref:`mvdelim_out2` )。
``v=`` のように値を指定しなければ空文字と見なされ、
結果として区切り文字が消去される( :numref:`mvdelim_out3` )。
文字列や漢字も指定することは可能であるが( :numref:`mvdelim_out4` )、
ベクトルを扱うコマンド(mvsortなど)で指定できる区切り文字
( ``delim=`` によって指定)はアルファベット１文字であるため、
もはやベクトルとして利用することはできなくなることに注意する。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mvdelim_input

  no,items
  1,b a a
  2,a a b b
  3,a b b a
  4,a b c




.. csv-table:: 基本例:区切りをマイナス記号に置換
  :header-rows: 1
  :name: mvdelim_out1

  no,items
  1,b-a-a
  2,a-a-b-b
  3,a-b-b-a
  4,a-b-c




.. csv-table:: 区切り文字にカンマを指定すると。。
  :header-rows: 1
  :name: mvdelim_out2

  no,items
  1,"b a a"
  2,"a a b b"
  3,"a b b a"
  4,"a b c"




.. csv-table:: 空文字を指定すると区切りが消える
  :header-rows: 1
  :name: mvdelim_out3

  no,items
  1,baa
  2,aabb
  3,abba
  4,abc




.. csv-table:: 複数文字も指定できるが。。
  :header-rows: 1
  :name: mvdelim_out4

  no,items
  1,bxxaxxa
  2,axxaxxbxxb
  3,axxbxxbxxa
  4,axxbxxc



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
param['kwd']='vf'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
区切り文字を変更するベクトル項目名を指定する。複数項目指定可能。
結果の項目名を変更したいときは、:(コロン)に続けて新項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='v'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
新しい区切り文字を指定する。何も指定しなければ空文字として扱われる。
'''
db['params'].append(param)

param={}
param['kwd']='A'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``vf=`` で:(コロン)に続けて指定した項目名で、新たな項目が追加される。
なお ``A`` オプションを指定した場合、 ``vf=`` パラメータで指定するすべての
項目に新項目名を指定しなければならない。
'''
db['params'].append(param)

param={}
param['kwd']='delim'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
ベクトル型データの区切り文字を指定する。
'''
db['params'].append(param)

db['comParams']='i,o,delim,assert_diffSize,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
