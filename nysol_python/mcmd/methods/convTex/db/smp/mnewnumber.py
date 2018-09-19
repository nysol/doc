# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mnewnumber'

############################### IDATA
db['idatas']=[]

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
1から始まる間隔が1の連番をふり、 ``No.`` という項目名で新規に5行のデータを作成する。
'''
script['sh_code']='''
mnewnumber a=No. I=1 S=1 l=5 o=rsl1.csv
'''
script['py_code']='''
nm.mnewnumber(a="No.", I="1", S="1", l="5", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='開始番号と間隔の変更'
script['comment']='''
10から始まる間隔が5の連番をふり、 ``No.`` という項目名で新規に5行のデータを作成する。
'''
script['sh_code']='''
mnewnumber a=No. I=5 S=10 l=5 o=rsl2.csv
'''
script['py_code']='''
nm.mnewnumber(a="No.", I="5", S="10", l="5", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='アルファベット連番'
script['comment']='''
Aから始まる間隔が1のアルファベット連番をふり、 ``No.`` という項目名で新規に5行のデータを作成する。
'''
script['sh_code']='''
mnewnumber a=No. I=1 S=A l=5 o=rsl3.csv
'''
script['py_code']='''
nm.mnewnumber(a="No.", I="1", S="A", l="5", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='ヘッダ行なしで新規作成'
script['comment']='''
Bから始まる間隔が3のアルファベット連番をふり、ヘッダなしで新規に11行のデータを作成する。
'''
script['sh_code']='''
mnewnumber  -nfn  I=3 l=11 S=B o=rsl4.csv
'''
script['py_code']='''
nm.mnewnumber(nfn=True, I="3", l="11", S="B", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

