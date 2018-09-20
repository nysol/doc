# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='regexs'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,str
1,caabaa
2,acabaaa
3,
4,cbcbcc
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``id=1,id=2`` 共に、正規表現で示された ``c`` に続く ``aa`` を含んでいるので真を返す。
'''
script['sh_code']='''
mcal c='regexs($s{str},"c.*aa")' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='regexs($s{str},"c.*aa")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='先頭一致'
script['comment']='''
正規表現 ``.*c`` を$str$項目が含むのは ``id=3`` 以外全ての行である。
'''
script['sh_code']='''
mcal c='regexs($s{str},".*c")' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='regexs($s{str},".*c")', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

