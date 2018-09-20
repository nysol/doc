# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='countnull'
db['title']='合計'
db['forms']=[
  ["countnull","num_1,num_2,...","m,m,r",""],
  ["countnull","str_1,str_2,...","m,m,r",""],
  ["countnull","date_1,date_2,...","m,m,r",""],
  ["countnull","time_1,time_2,...","m,m,r",""],
  ["countnull","bool_1,bool_2,...","m,m,r",""]
]
############################### DOCUMENT
db['doc']='''
:math:`num_i` (その他の型も同様)で与えられた数値の中でNULL値の数を返す。
'''

