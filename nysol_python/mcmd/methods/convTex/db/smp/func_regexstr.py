# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='regexstr'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,str
1,xcbbbayy
2,xxcbaay
3,
4,bacabbca
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
正規表現 ``c.*a`` に最も長くマッチする部分文字列を得る。
``id=2`` では、 ``cba`` もしくは ``cbaa`` いずれの部分文字列にもマッチしたと考えることができるが、
本関数では、より長くマッチした文字列を返す。
'''
script['sh_code']='''
mcal c='regexstr($s{str},"c.*a")' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='regexstr($s{str},"c.*a")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

