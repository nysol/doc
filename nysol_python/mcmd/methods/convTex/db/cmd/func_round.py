# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='round'
db['title']='四捨五入'
db['forms']=[
  ["round","num,基数","m,m",""]
]
############################### DOCUMENT
db['doc']='''
:math:`num` を四捨五入によりまるめる。
この時、基数の整数倍の値集合のうち最も近い値にまるめられる。
例えば、round(3.82,0.5)の場合、0.5とびに目盛がうたれた数直線上で、
3.82に最も近い目盛点、すなわち4.0が基数0.5における四捨五入点となる。
基数を省略すると1.0がデフォルト値として用いられる。
これは小数点以下1桁目を四捨五入して整数値にまるめることに等しい。
'''
