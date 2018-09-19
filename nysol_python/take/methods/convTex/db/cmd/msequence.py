# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='msequence'
db['title']='多頻度系列パターンの列挙'
db['related']=[
  ["mitemset","アイテム集合列挙ならこちら"]
]

############################### DOCUMENT
db['doc']='''
多頻度系列パターンを列挙する。
内部的には、 :doc:`Takeのコアメソッドlcmseq <../methods0/lcmseq>` を用いている。
'''

############################### PARAMETERS
db['params']=[]

param={}
param['kwd']='i'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
系列データファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='O'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='./take_現在日付時刻'
param['text']='''
出力ディレクトリ名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='x'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='階層分類を使わない'
param['text']='''
taxonomyファイル名を指定する。
``item`` 項目の値を対応するtaxonomyに変換して実行する。例えば、アイテムa,bのtaxonomyをX、c,dのtaxonomyをYとすると、
シーケンス aeadd は XeXYY に変換される。
'''
db['params'].append(param)

param={}
param['kwd']='tid'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='tid'
param['text']='''
トランザクションID項目名(i=上の項目名)
'''
db['params'].append(param)

param={}
param['kwd']='time'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='time'
param['text']='''
系列の順序関係を表す時間項目名を指定する。
'''
db['params'].append(param)


param={}
param['kwd']='item'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='item'
param['text']='''
アイテム項目名(i=,t=上の項目名)
'''
db['params'].append(param)

param={}
param['kwd']='cls'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='class'
param['text']='''
クラス項目名(c=上の項目名)
'''
db['params'].append(param)

param={}
param['kwd']='taxo'
param['type']='str'
param['mand']=True
param['cond']='x=指定時'
param['default']=''
param['text']='''
'''
db['params'].append(param)

param={}
param['kwd']='s'
param['type']='float'
param['mand']=False
param['cond']=''
param['default']='0.05'
param['text']='''
最小支持度(全トランザクション数に対する割合による指定)
'''
db['params'].append(param)

param={}
param['kwd']='S'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='1'
param['text']='''
最小支持度(件数による指定)
s=,S=共に指定しなければ、s=0.05が指定されたことになる。
両方指定されれば、S=が優先される。
'''
db['params'].append(param)

param={}
param['kwd']='sx'
param['type']='float'
param['mand']=False
param['cond']=''
param['default']='1.0'
param['text']='''
最大支持度(全トランザクション数に対する割合による指定)
'''
db['params'].append(param)

param={}
param['kwd']='Sx'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
最大支持度(件数による指定)
sx=,Sx=共に指定しなければ、sx=1.0が指定されたことになる。
両方指定されれば、Sx=が優先される。
'''
db['params'].append(param)

param={}
param['kwd']='l'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
パターンサイズの下限(1以上20以下の整数)
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
パターンサイズの上限(1以上20以下の整数)
'''
db['params'].append(param)

param={}
param['kwd']='p'
param['type']='float'
param['mand']=False
param['cond']=''
param['default']='0.5'
param['text']='''
最小事後確率
'''
db['params'].append(param)

param={}
param['kwd']='g'
param['type']='float'
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
最小増加率
p=,g=共に指定しなければ、p=0.5が指定されたことになる。
両方指定されれば、g=が優先される。
'''
db['params'].append(param)

param={}
param['kwd']='gap'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='0'
param['text']='''
パターンのギャップ長の上限(0以上の整数)を指定する。
0を指定すれば制限なしとなる。
'''
db['params'].append(param)

param={}
param['kwd']='win'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='0'
param['text']='''
パターンのウィンドウサイズの上限(0以上の整数)を指定する。
0を指定すれば制限なしとなる。
'''
db['params'].append(param)

param={}
param['kwd']='padding'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
時刻を整数とみなし、連続でない時刻に特殊なアイテムがあることを想定する。
``gap=`` や ``win=`` の指定に影響する。
パターンのウィンドウサイズの上限(0以上の整数)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='top'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
列挙するパターン数の上限を指定する。
例えばtop=10と指定すると、支持度が10番目高いパターンの支持度を最小支持度として頻出パターンを列挙する。
よって、同じ支持度のパターンが複数個ある場合は10個以上のパターンが列挙されるかもしれない。
'''
db['params'].append(param)

param={}
param['kwd']='T'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='/tmp'
param['text']='''
ワークディレクトリを指定する。
'''
db['params'].append(param)

db['comParams']=''
