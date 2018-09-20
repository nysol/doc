# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='regexm'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,str
1,caabaa
2,acabaaa
3,
4,bbcbcc
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``id=1,id=2`` 共に、正規表現で示された ``c`` に続く ``aa`` を含んでいるが、
``id=2`` ではマッチする範囲が部分的(2文字目の ``c`` から最後まで)であるために偽となっている。
'''
script['sh_code']='''
mcal c='regexm($s{str},"c.*aa")' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='regexm($s{str},"c.*aa")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='末尾一致'
script['comment']='''
正規表現 ``.*c`` で$str$項目の全体がカバーされるのは ``id=4`` の行のみである。
'''
script['sh_code']='''
mcal c='regexm($s{str},".*c")' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='regexm($s{str},".*c")', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='空文字マッチ'
script['comment']='''
正規表現 ``^$`` で ``id=3`` の空文字にマッチする。
'''
script['sh_code']='''
mcal c='regexm($s{str},"^$")' a=rsl i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='regexm($s{str},"^$")', a='rsl', i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

