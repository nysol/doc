# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mtra'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,item
A,a
A,b
B,c
B,d
B,e
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``customer`` を単位に ``item`` をスペース区切りで結合し、
``transaction`` という項目名で出力する。
'''
script['sh_code']='''
mtra k=customer f=item:transaction i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mtra(k="customer", f="item:transaction", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='アイテムの区切り文字を-(ハイフン）で実行'
script['comment']='''
'''
script['sh_code']='''
mtra k=customer f=item:transaction delim=- i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mtra(k="customer", f="item:transaction", delim="-", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='アイテムを降順に並べ替えてから変換'
script['comment']='''
'''
script['sh_code']='''
mtra k=customer s=item%r f=item:transaction i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mtra(k="customer", s="item%r", f="item:transaction", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

