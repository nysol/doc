# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='cat'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,str1,str2,str3
1,abc,def,ghi
2,A,,CDE
3,,,
4,,,XY
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
3つの項目str1,str2,str3を ``"#"`` の区切り文字を挿入して併合する。
'''
script['sh_code']='''
mcal c='cat("#",$s{str1},$s{str2},$s{str3})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='cat("#",$s{str1},$s{str2},$s{str3})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='tokenが空文字の場合'
script['comment']='''
'''
script['sh_code']='''
mcal c='cat("",$s{str1},$s{str2},$s{str3})' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='cat("",$s{str1},$s{str2},$s{str3})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='ワイルドカードを利用した例'
script['comment']='''
``str`` から始まる項目( ``str1,str2,str3`` )をワイルドカード「 ``str*`` 」によって指定している。
'''
script['sh_code']='''
mcal c='cat("",$s{str*})' a=rsl i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='cat("",$s{str*})', a='rsl', i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

