# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='if'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,time
1,101215
2,210110
3,
4,120001
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
id,val
1,1
2,0
3,
4,-2
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
script['title']='基本例'
script['comment']='''
time項目が数値として120000以下であれば"AM"、そうでなければ"PM"を出力する。
'''
script['sh_code']='''
mcal c='if(${time}<=120000,"AM","PM")' a=ampm i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='if(${time}<=120000,"AM","PM")', a='ampm', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='真偽値による条件選択'
script['comment']='''
``$b{項目名}`` によって、データ上の値"1"は真、
"0"は偽、そしてその他の値はNULLとして解釈される。
'''
script['sh_code']='''
mcal c='if($b{val},"true","false")' a=bool i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='if($b{val},"true","false")', a='bool', i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='時刻型として比較'
script['comment']='''
'''
script['sh_code']='''
mcal c='if($t{time}<=0t120000,"am","pm")' a=ampm i=dat1.csv o=rsl4.csv
'''
script['py_code']='''
nm.mcal(c='if($t{time}<=0t120000,"am","pm")', a='ampm', i="dat1.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='if関数のネスト'
script['comment']='''
'''
script['sh_code']='''
mcal c='if(${val}>0,"plus",if(${val}<0,"minus","zero"))' a=sign i=dat3.csv o=rsl5.csv
'''
script['py_code']='''
nm.mcal(c='if(${val}>0,"plus",if(${val}<0,"minus","zero"))', a='sign', i="dat3.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

