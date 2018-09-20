# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='or'
db['title']='論理和'
db['forms']=[
  ["or","bool_1,bool_2,...","m,m,r",""]
]
############################### DOCUMENT
db['doc']='''
:math:`bool_i` で与えられた真偽値全ての論理和を計算する。
NULL値を含めた真偽値表は表\ref{tbl:mcal_or}を参照のこと。
'''

