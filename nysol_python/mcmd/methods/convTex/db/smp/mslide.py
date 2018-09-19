# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mslide'

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

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
'''
script['sh_code']='''
mslide s=date f=val:newVal i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mslide(s="date", f="val:newVal", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='逆にずらした例'
script['comment']='''
'''
script['sh_code']='''
mslide s=date f=val:newVal -r i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mslide(s="date", f="val:newVal", r=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='複数回指定した場合'
script['comment']='''
'''
script['sh_code']='''
mslide s=date f=val t=2 i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mslide(s="date", f="val", t="2", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='最後にずらした項目だけを出力する例'
script['comment']='''
'''
script['sh_code']='''
mslide s=date f=val t=2 -l i=dat1.csv o=rsl4.csv
'''
script['py_code']='''
nm.mslide(s="date", f="val", t="2", l=True, i="dat1.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='複数項目名を変更して出力する例'
script['comment']='''
'''
script['sh_code']='''
mslide s=date f=date:d_,val:v_ t=2 i=dat1.csv o=rsl5.csv
'''
script['py_code']='''
nm.mslide(s="date", f="date:d_,val:v_", t="2", i="dat1.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

