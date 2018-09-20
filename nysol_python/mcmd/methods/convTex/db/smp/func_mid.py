# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mid'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,str
1,abcdefg
2,12345678
3,
4,12
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,str
1,あいうえお
2,1234567あ8
3,1あ
4,ああ
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
str項目の2文字目からから3文字を切り出す。
'''
script['sh_code']='''
mcal c='mid($s{str},2,3)' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='mid($s{str},2,3)', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='基本例'
script['comment']='''
マルチバイト文字を含む場合はmidwを使う。
'''
script['sh_code']='''
mcal c='midw($s{str},2,3)' a=rsl i=dat2.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='midw($s{str},2,3)', a='rsl', i="dat2.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

