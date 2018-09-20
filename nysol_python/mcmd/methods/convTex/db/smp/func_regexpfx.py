# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='regexpfx'

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
正規表現 ``c.*a`` に最も長くマッチする部分文字列のプレフィックスを得る。
例えば ``id=4`` では、$str$項目の ``cabbca`` にマッチしており、そのプレフィックス
すなわち ``ba`` を返している。
``regexstr,regexpfx`` と同じ入力データを使っているので、比較すると分かりやすい。
'''
script['sh_code']='''
mcal c='regexpfx($s{str},"c.*a")' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='regexpfx($s{str},"c.*a")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

