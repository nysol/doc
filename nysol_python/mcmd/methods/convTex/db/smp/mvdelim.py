# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mvdelim'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
item1
b a c
c c
e a a
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
ベクトル型要素のデフォルトの区切り文字である半角スペースを ``_`` (アンダーバー)に置換する。
'''
script['sh_code']='''
mvdelim vf=item1 v=_ i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mvdelim(vf="item1", v="_", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='カンマ'
script['comment']='''
CSVの区切り文字であるカンマに置換すると、CSVの区切り文字との区別を付けるために、
ベクトル全体がダブルクオーツで囲われる。
'''
script['sh_code']='''
mvdelim vf=item1 v=, i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mvdelim(vf="item1", v=",", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

