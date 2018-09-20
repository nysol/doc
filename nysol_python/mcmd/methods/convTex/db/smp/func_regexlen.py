# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='regexlen'

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

data={}
data['name']='dat2.csv'
data['text']='''
id,str
1,漢漢あbbbいyy
2,漢あbいいy
3,
4,bあいあbbいあ
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
正規表現 ``c.*a`` に最も長くマッチする部分文字列の長さを得る。
マッチした部分文字列については ``regexstr`` と同じ入力データを使っているので、比較すると分かりやすい。
'''
script['sh_code']='''
mcal c='regexlen($s{str},"c.*a")' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='regexlen($s{str},"c.*a")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='マルチバイト文字'
script['comment']='''
正規表現 ``"あ.*い"`` に最も長くマッチする部分文字列の長さを得る。
ただし、以下ではマルチバイト文字対応でないregexlen関数を使っているので、
文字数ではなくバイト数を返している。
'''
script['sh_code']='''
mcal c='regexlen($s{str},"あ.*い")' a=rsl i=dat2.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='regexlen($s{str},"あ.*い")', a='rsl', i="dat2.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='マルチバイト文字2'
script['comment']='''
正規表現 ``"あ.*い"`` に最も長くマッチする部分文字列の長さを得る。
regexlenw関数を使うと、正しくマルチバイト文字を扱ってくれる。
'''
script['sh_code']='''
mcal c='regexlenw($s{str},"あ.*い")' a=rsl i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='regexlenw($s{str},"あ.*い")', a='rsl', i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

