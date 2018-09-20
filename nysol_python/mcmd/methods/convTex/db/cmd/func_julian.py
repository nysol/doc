# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='julian'
db['title']='ユリウス暦変換'
db['forms']=[
  ["julian","date","m",""],
  ["julian","time","m",""],
  ["julian2d","num","m",""],
  ["julian2t","num","m",""]
]
############################### DOCUMENT
db['doc']='''
書式1,2では、日付 :math:`date` もしくは時刻 :math:`time` をユリウス通日に変換する。
逆に書式3,4では、ユリウス通日を日付型もしくは時刻型に変換する。
ここで、日付型が与えられたときは、その日の最初の時刻である ``00:00:00`` として計算される。
'''

