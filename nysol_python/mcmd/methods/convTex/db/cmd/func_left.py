# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='left'
db['title']='先頭切り出し'
db['forms']=[
  ["left","str,長さ","m,m",""],
  ["leftw","str,長さ","m,m",""]
]
############################### DOCUMENT
db['doc']='''
文字列 :math:`str` について先頭から長さパラメータで指定した文字数を切り出す。
マルチバイト文字を含む場合はleftwを使うこと。
'''
