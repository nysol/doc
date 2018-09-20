# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mcat'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,date,amount
A,20081201,10
B,20081002,40
'''
db['idatas'].append(data)

data={}
data['name']='dat2.csv'
data['text']='''
customer,date,amount
A,20081207,20
A,20081213,30
B,20081209,50
'''
db['idatas'].append(data)

data={}
data['name']='dat3.csv'
data['text']='''
customer,date,quantity
A,20081201,3
B,20081002,1
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='同一項目名ファイルの併合'
script['comment']='''
'''
script['sh_code']='''
mcat i=dat1.csv,dat2.csv o=rsl1.csv
'''
script['py_code']='''
nm.mcat(i="dat1.csv,dat2.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='項目名の異なるファイルの併合'
script['comment']='''
``i=`` の最初のファイル ``dat1.csv`` の項目「顧客,日付,金額」の3項目を併合する。
しかし、 ``dat3.csv`` には ``amount`` 項目がないので、エラーとなる。
ただし、 ``dat1.csv`` の内容は既に出力されていることに注意する。
'''
script['sh_code']='''
mcat i=dat1.csv,dat3.csv o=rsl2.csv
'''
script['py_code']='''
nm.mcat(i="dat1.csv,dat3.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='項目名の異なるファイルの併合2'
script['comment']='''
前例に ``nostop=True`` オプションを付けると、項目が見つからないデータについてはNULL値を出力するようになり、
途中でエラー終了することはなくなる。
その他にも、項目が見つからなかった場合の動作を変更するオプションとして、 ``skip`` , ``force`` がある。
詳しくはパラメータの説明を参照されたい。
'''
script['sh_code']='''
mcat -nostop i=dat1.csv,dat3.csv o=rsl3.csv
'''
script['py_code']='''
nm.mcat(nostop=True, i="dat1.csv,dat3.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='項目名を指定して併合'
script['comment']='''
``f=`` で項目名を指定すると、それら指定した項目のみを併合する。
'''
script['sh_code']='''
mcat f=顧客,日付 i=dat2.csv,dat3.csv o=rsl4.csv
'''
script['py_code']='''
nm.mcat(f="customer,date", i="dat2.csv,dat3.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='標準入力の併合'
script['comment']='''
``stdin=True`` を指定することで、 ``dat2.csv`` を標準入力から追加する。
'''
script['sh_code']='''
mcat -stdin i=dat1.csv o=rsl5.csv <dat2.csv
'''
script['py_code']='''
'''
script['odatas']=''
db['scripts'].append(script)

script={}
script['title']='ファイル名項目を追加'
script['comment']='''
``add_fname`` オプションを指定すると、元ファイルの名前を ``fileName`` 項目で追加する。
標準入力のファイル名は ``/dev/stdin`` となる。
'''
script['sh_code']='''
mcat -add_fname -stdin i=dat1.csv o=rsl6.csv <dat2.csv
'''
script['py_code']='''
'''
script['odatas']=''
db['scripts'].append(script)

script={}
script['title']='ワイルドカード指定'
script['comment']='''
カレントディレクトリに ``dat1.csv,dat2.csv,dat3.csv`` の3つのCSVファイルがあったとして、
それらを全て併合するのにワイルドカード ``dat*.csv`` を指定する。
'''
script['sh_code']='''
mcat -force i=dat*.csv o=rsl7.csv
'''
script['py_code']='''
nm.mcat(force=True, i="dat*.csv", o="rsl7.csv").run()
'''
script['odatas']='rsl7.csv'
db['scripts'].append(script)

script={}
script['title']='同一ファイルの複数回併合'
script['comment']='''
同一ファイルを複数指定することも可能である。
'''
script['sh_code']='''
mcat i=dat1.csv,dat1.csv,dat1.csv o=rsl8.csv
'''
script['py_code']='''
nm.mcat(i="dat1.csv,dat1.csv,dat1.csv", o="rsl8.csv").run()
'''
script['odatas']='rsl8.csv'
db['scripts'].append(script)

