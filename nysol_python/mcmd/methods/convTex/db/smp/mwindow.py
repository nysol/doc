# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mwindow'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
date,val
20130406,1
20130407,2
20130408,3
20130409,4
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
store,date,val
a,20130406,1
a,20130407,2
a,20130408,3
a,20130409,4
b,20130406,11
b,20130407,12
b,20130408,13
b,20130409,14
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mwindow wk=date:win t=2 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mwindow(wk="date:win", t="2", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='基準行を先頭にした例'
script['comment']='''
'''
script['sh_code']='''
mwindow wk=date:win t=3 -r i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mwindow(wk="date:win", t="3", r=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='指定行数に満たない窓も出力する例'
script['comment']='''
'''
script['sh_code']='''
mwindow wk=date:win t=3 -r -n i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mwindow(wk="date:win", t="3", r=True, n=True, i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='キー項目を指定した例'
script['comment']='''
'''
script['sh_code']='''
mwindow k=store wk=date:win t=2 i=dat2.csv o=rsl4.csv
'''
script['py_code']='''
nm.mwindow(k="store", wk="date:win", t="2", i="dat2.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='前日までの移動平均を求める'
script['comment']='''
冒頭に示した移動平均の例では、窓における最終日を基準として平均を計算している。
時に、基準日を前日として移動平均を計算したいケースがある。
そういった場合は ``mslide`` で1日日付をずらしてから本コマンドを使えばよい。
その例を以下に示す。
'''
script['sh_code']='''
mslide f=date:date2 s=date i=dat1.csv o=rsl5.csv
mwindow wk=date2:win t=2 i=rsl5.csv o=rsl6.csv
'''
script['py_code']='''
nm.mslide(f="date:date2", s="date", i="dat1.csv", o="rsl5.csv").run()
nm.mwindow(wk="date2:win", t="2", i="rsl5.csv", o="rsl6.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

