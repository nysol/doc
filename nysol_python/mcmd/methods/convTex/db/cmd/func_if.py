# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='if'
db['title']='条件選択'
db['forms']=[
	["if","bool,num1,num2","m,m,m",""],
	["if","bool,str1,str2","m,m,m",""],
	["if","bool,date1,date2","m,m,m",""],
	["if","bool,time1,time2","m,m,m",""],
	["if","bool,bool1,bool2","m,m,m",""]
]
############################### DOCUMENT
db['doc']='''
第1パラメータの値が真であれば第2パラメータを、偽であれば第3パラメータを返す。
第1パラメータがNULL値であればNULL値を返す。
第2パラメータと第3パラメータは同じ型でなくてはならないことに注意する。
'''

