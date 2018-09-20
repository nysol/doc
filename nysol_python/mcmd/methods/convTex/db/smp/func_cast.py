# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='cast'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id
1
2
3
4
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,v1,v2,v3
1,10,5,7
2,5,12,11
3,3,6,2
4,14,16,11
'''
db['idatas'].append(data)

data={}
data['name']='dat3.csv'
data['text']='''
id,val
1,10
2,0
3,-5
4,0
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='乱数の固定長化'
script['comment']='''
1から9999の整数乱数を発生させ、4桁固定長で出力する。
fixlen関数は整数型のデータ(ここではrandiの結果)には対応していないので、
n2s関数で文字列型に変換する必要がある。
'''
script['sh_code']='''
mcal c='fixlen(n2s(randi(1,9999,11)),4,"R","0")' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='fixlen(n2s(randi(1,9999,11)),4,"R","0")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='真偽パターン'
script['comment']='''
項目v1,v2,v3が10異常かどうかを判定し、01のパターンを出力する。
'''
script['sh_code']='''
mcal c='cat("",b2s(${v1}>=10),b2s(${v2}>=10),b2s(${v3}>=10))' a=rsl i=dat2.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='cat("",b2s(${v1}>=10),b2s(${v2}>=10),b2s(${v3}>=10))', a='rsl', i="dat2.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

