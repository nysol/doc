# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='dow'
db['title']='曜日'
db['forms']=[
  ["dow","date","m","曜日番号(1〜7)"],
  ["dow","time","m","曜日番号(1〜7)"],
  ["dowj","date","m","日本語曜日"],
  ["dowj","time","m","日本語曜日"],
  ["dowe","date","m","英語曜日"],
  ["dowe","time","m","英語曜日"],
  ["dowes","date","m","英語短縮曜日"],
  ["dowes","time","m","英語短縮曜日"]
]
############################### DOCUMENT
db['doc']='''
日付 :math:`date` もしくは時刻 :math:`time` から曜日を返す。
曜日の表記によって書式1〜8を使い分ける。
曜日番号は、ISO8601の規定に従い、1が月曜日で7が日曜日に対応する。
'''

