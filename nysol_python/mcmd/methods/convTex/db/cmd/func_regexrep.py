# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='regexrep'
db['title']='マッチ文字列の置換'
db['forms']=[
  ["regexrep","str,正規表現,置換文字列","m,m,m",""],
  ["regexrepw","str,正規表現,置換文字列","m,m,m",""]
]
############################### DOCUMENT
db['doc']='''
指定した正規表現が最長マッチした文字列 :math:`str` の部分文字列を置換文字列で置換する。
:math:`str` もしくは正規表現にマルチバイト文字を含み
Shift\_JISなど文字の出現順によっては意に沿わない検索結果となる場合はregexrepw関数を使うこと。
'''

