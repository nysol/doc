# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mtab2csv'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.tab'
data['text']='''
id	data	data2
A	1102	a
A	2203	aaa
B	1155	bbbb
B	3104	c
B	1206	de
'''
db['idatas'].append(data)

data={}
data['name']='dat2.bar'
data['text']='''
id-data-data2
A-1102-a
A-2203-aaa
B-1155-bbbb
B-3104-c
B-1206-de
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
タブ区切りデータをcsvへ変換
'''
script['sh_code']='''
mtab2csv i=dat1.tab o=rsl1.csv
'''
script['py_code']='''
nm.mtab2csv(i="dat1.tab", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='d=指定'
script['comment']='''
``d=`` を使用してtab以外の区切り文字を使う
'''
script['sh_code']='''
mtab2csv d=- i=dat2.bar o=rsl2.csv
'''
script['py_code']='''
nm.mtab2csv(d="-", i="dat2.bar", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

