# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='diff'
db['title']='期間'
db['forms']=[
  ["diffyear","date_1,date_2","m,m",""],
  ["diffyear","time_1,time_2","m,m",""],
  ["diffmonth","date_1,date_2","m,m",""],
  ["diffmonth","time_1,time_2","m,m",""],
  ["diffday","date_1,date_2","m,m",""],
  ["diffday","time_1,time_2","m,m",""],
  ["diffhour","time_1,time_2","m,m",""],
  ["diffminute","time_1,time_2","m,m",""],
  ["diffsecond","time_1,time_2","m,m",""],
  ["diffusecond","time_1,time_2","m,m",""]
]
############################### DOCUMENT
db['doc']='''
二つの引数が日付型の場合、 :math:`date_1` と :math:`date_2` の差( :math:`date_1-date_2` )を計算し、
その年数(difyear)、月数(diffmonth)、日数(diffday)で計算する。
二つの引数が時刻型の場合、 :math:`time_1` と :math:`time_2` の差( :math:`time_1-time_2` )を計算し、
その年数(difyear)、月数(diffmonth)、日数(diffday)、
時間数(diffhour)、分数(diffminute)、秒数(diffsecond)、マイクロ秒数(diffusecond)で計算する。
端数は切り捨てられる。
'''

