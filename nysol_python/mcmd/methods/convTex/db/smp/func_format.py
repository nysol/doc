# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='format'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,val
1,0.00726
2,123.456789
3,
4,-0.335
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,amount
1,1000
2,250
3,
4,960
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``val`` を実数として小数点以下2桁に変換する。
'''
script['sh_code']='''
mcal c='format(${val},"%8.3f")' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='format(${val},"%8.3f")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='指数表現'
script['comment']='''
``val`` を指数表現で出力。
'''
script['sh_code']='''
mcal c='format(${val},"%e")' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='format(${val},"%e")', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='文字列との組み合せ'
script['comment']='''
'''
script['sh_code']='''
mcal c='format(${amount},"total amount is %g yen.")' a=rsl i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='format(${amount},"total amount is %g yen.")', a='rsl', i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

