# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='fixlen'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,str
1,abc
2,123
3,
4,1234567
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,str
1,こんにちは
2,大阪
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
str項目を5文字の固定長文字列に変換する。
5文字に満たない文字列は右詰( ``"R"`` )で ``"#"`` を埋める。
'''
script['sh_code']='''
mcal c='fixlen($s{str},5,"R","#")' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='fixlen($s{str},5,"R","#")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='左詰め例'
script['comment']='''
左詰( ``"L"`` )で ``"#"`` を埋める。
'''
script['sh_code']='''
mcal c='fixlen($s{str},5,"L","#")' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='fixlen($s{str},5,"L","#")', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='マルチバイト文字を含む場合'
script['comment']='''
'''
script['sh_code']='''
mcal c='fixlenw($s{str},4,"R","埋")' a=rsl i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='fixlenw($s{str},4,"R","埋")', a='rsl', i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

