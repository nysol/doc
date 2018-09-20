# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='regexpos'
db['title']='マッチ位置'
db['forms']=[
  ["regexpos","str,正規表現","m,m",""],
  ["regexposw","str,正規表現","m,m",""]
]
############################### DOCUMENT
db['doc']='''
指定した正規表現が最長マッチする文字列 :math:`str` の部分文字列の開始位置を返す。
文字列の先頭位置は0であることに注意する。またマッチしなければNULL値を返す。
:math:`str` もしくは正規表現にマルチバイト文字を含む場合はregexposw関数を使うこと。
'''

