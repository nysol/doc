# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='sum'
db['title']='合計'
db['forms']=[
  ["sum","num_1,num_2,...","m,m,r",""],
  ["sum","num_1,num_2,...,str","m,m,r,m",""]
]
############################### DOCUMENT
db['doc']='''
:math:`num_i` で与えられた数値を全て合計する。
書式1では、NULL値は無視されるが、全てがNULL値であれば結果もNULLとなる。
書式2において最後の引数として"-n"を与えると、
NULL値に対する扱いが変わり、
項目値に一つでもNULL値がある場合は、結果もNULL値となる。
'''
