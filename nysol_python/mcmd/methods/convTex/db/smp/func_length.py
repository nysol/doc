# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='length'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,str
1,abc
2,3.1415
3,
4,hello world!
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
'''
script['sh_code']='''
mcal c='length($s{str})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='length($s{str})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='マルチバイト文字を含む例'
script['comment']='''
以下はutf-8でエンコーディングされた日本語を用いた例である。
utf-8の日本語は1文字3バイトでエンコーディングされているので、
length関数では日本語としての文字数ではなく、そのバイト数を返す。
'''
script['sh_code']='''
mcal c='length($s{str})' a=rsl i=dat2.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='length($s{str})', a='rsl', i="dat2.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='ワイド文字として扱う例'
script['comment']='''
lengthwを使うと、内部で文字列をワイド文字に変換するので、マルチバイト文字1文字を正しく認識して計算する。
'''
script['sh_code']='''
mcal c='lengthw($s{str})' a=rsl i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='lengthw($s{str})', a='rsl', i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

