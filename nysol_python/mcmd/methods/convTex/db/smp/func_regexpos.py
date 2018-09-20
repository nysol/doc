# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='regexpos'

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
正規表現 ``c.*a`` に最も長くマッチする部分文字列の位置を得る。
先頭文字の位置は0であることに注意する。
マッチした部分文字列については ``regexstr`` と同じ入力データを使っているので、比較すると分かりやすい。
'''
script['sh_code']='''
mcal c='regexpos($s{str},"c.*a")' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='regexpos($s{str},"c.*a")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='マルチバイト文字'
script['comment']='''
正規表現 ``"い.*あ"`` に最も長くマッチする部分文字列の長さを得る。
ただし、以下ではマルチバイト文字対応でないregexpos関数を使っているので、
文字数ではなくバイト数でカウントした場合の位置を返している。
'''
script['sh_code']='''
mcal c='regexpos($s{str},"あ.*い")' a=rsl i=dat2.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='regexpos($s{str},"あ.*い")', a='rsl', i="dat2.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='マルチバイト文字2'
script['comment']='''
正規表現 ``"い.*あ"`` に最も長くマッチする部分文字列の長さを得る。
regexposw関数を使うと、正しくマルチバイト文字を扱ってくれる。
'''
script['sh_code']='''
mcal c='regexposw($s{str},"あ.*い")' a=rsl i=dat2.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcal(c='regexposw($s{str},"あ.*い")', a='rsl', i="dat2.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

