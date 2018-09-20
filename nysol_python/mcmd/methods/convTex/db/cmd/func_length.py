# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='length'
db['title']='文字列長'
db['forms']=[
  ["length","str","m",""],
  ["lengthw","str","m",""]
]
############################### DOCUMENT
db['doc']='''
文字列の長さを計算する。
lengthw関数を用いると、 :math:`str` をワイド文字として扱う。
NULL値の長さは0であることに注意する。
'''

