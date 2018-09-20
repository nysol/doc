# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='regexpfx'
db['title']='マッチ文字列のプレフィックス'
db['forms']=[
  ["regexpfx","str,正規表現","m,m",""],
  ["regexpfxw","str,正規表現","m,m",""]
]
############################### DOCUMENT
db['doc']='''
指定した正規表現が最長マッチする文字列 :math:`str` の部分文字列のプレフィックス
(部分文字列より先頭側の文字列)を返す。
同じ文字列及び正規表現によってregexpfx関数,regexstr関数,regexsfx関数の3関数を実行した場合、
それぞれで得られた文字列をその順番に結合すると元の文字列が再現できる関係にある。
:math:`str` もしくは正規表現にマルチバイト文字を含み、
Shift\_JISなど文字の出現順によっては意に沿わない検索結果となる場合はregexpfxw関数を使うこと。
'''

