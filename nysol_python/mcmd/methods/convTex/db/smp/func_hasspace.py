# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='hasspace'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,str
1,a b
2,ab	c
3,ab　c
4,
5,"aa
bb"
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``str`` 項目に空白類文字列が含まれていれば真を返す。
``id=1`` の行は半角スペース文字が含まれ、
``id=2`` の行はtab文字が含まれ、
そして ``id=4`` の行は改行文字が含まれているために真となっている。
ここで、 ``id=3`` の行は全角スペースのため、検知できていない。
'''
script['sh_code']='''
mcal c='hasspace($s{str})' a=rsl i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcal(c='hasspace($s{str})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='マルチバイト文字'
script['comment']='''
hasspacew関数を使えば全角スペースも正しく検知できる。
'''
script['sh_code']='''
mcal c='hasspacew($s{str})' a=rsl i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcal(c='hasspacew($s{str})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

