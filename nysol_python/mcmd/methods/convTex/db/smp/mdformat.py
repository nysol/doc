# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mdformat'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
fld
date:20120304 time:121212
date:20101204 time:011309.1234
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
fld,fld2
2010/11/20,2010/11/21
2010/1/1,2010/1/2
2011/01/01,2010/01/02
2010/1/01,2010/1/02
'''
db['idatas'].append(data)

data={}
data['name']='dat3.csv'
data['text']='''
fld
2010 11 20 12:34:56
2011 01 01 23:34:56
2010  1 01 123455
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``fld`` 項目から日付・時刻を抽出し変換する。
``fld`` 項目には「date:年月日 time:時分秒.マイクロ秒」の形式で日付・時刻が格納されているので、
``c=`` パラメータには「 ``date:%Y%m%d time:%H%M%s`` 」と指定している。
'''
script['sh_code']='''
mdformat f=fld c='date:%Y%m%d time:%H%M%s' i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mdformat(f="fld", c="date:%Y%m%d time:%H%M%s", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='項目の追加'
script['comment']='''
``fld1`` 項目、 ``fld2`` 項目には「年/月/日」形式で日付が格納されているので、
``c=`` パラメータには「 ``%Y/%m/%d`` 」と指定している。
``A=True`` オプションを使用し、変換結果を新たな ``f1`` 、 ``f2`` 項目に抽出する。
'''
script['sh_code']='''
mdformat f=fld:f1,fld2:f2 c=%Y/%m/%d i=dat2.csv -A o=rsl2.csv
'''
script['py_code']='''
nm.mdformat(f="fld:f1,fld2:f2", c="%Y/%m/%d", i="dat2.csv", A=True, o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='抽出がうまくいかない例'
script['comment']='''
``fld`` 項目には「年 月 日 時:分:秒」形式で日付が格納されているので、
``c=`` パラメータには「 ``%Y %m %d %H:%M:%S`` 」と指定している。
しかし形式が異なる行は抽出に失敗している。
'''
script['sh_code']='''
mdformat f=fld:f1 c='%Y %m %d %H:%M:%S' i=dat3.csv -A o=rsl3.csv
'''
script['py_code']='''
nm.mdformat(f="fld:f1", c="%Y %m %d %H:%M:%S", i="dat3.csv", A=True, o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

