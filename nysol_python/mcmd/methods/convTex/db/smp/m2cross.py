# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='m2cross'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
item,date,quantity
A,20081201,1
A,20081202,2
A,20081203,3
B,20081201,4
B,20081203,5
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
item,week,quantity
A,Monday,1
A,Tuesday,2
A,Wednesday,3
B,Thursday,4
B,Friday,5
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``item`` 項目を単位に ``date`` 項目を横に展開し、
``quantity`` 項目を出力する。
'''
script['sh_code']='''
m2cross k=item f=quantity s=date i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.m2cross(k="item", f="quantity", s="date", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='元の入力データに戻す例'
script['comment']='''
例1の出力結果を元に戻すには、同じく ``m2cross`` を以下のよう用いればよい。
'''
script['sh_code']='''
m2cross f=2008* a=date,quantity i=rsl1.csv o=rsl2.csv
'''
script['py_code']='''
nm.m2cross(f="2008*", a="date,quantity", i="rsl1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='並びを逆順する例'
script['comment']='''
横に展開する項目名の並びを逆順にする。
'''
script['sh_code']='''
m2cross k=item f=quantity s=date%r i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.m2cross(k="item", f="quantity", s="date%r", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='データがない場合に項目を追加する例'
script['comment']='''
横に展開する際に、データがない場合に項目を追加する"
'''
script['sh_code']='''
m2cross k=item f=quantity s=week i=dat2.csv fixfld=Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday o=rsl4.csv
'''
script['py_code']='''
nm.m2cross(k="item", f="quantity", s="week", i="dat2.csv", fixfld="Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

