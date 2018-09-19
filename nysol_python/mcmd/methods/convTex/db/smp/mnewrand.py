# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mnewrand'

############################### IDATA
db['idatas']=[]

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
実数乱数を10行生成する。乱数の種は1に固定しているので、いつ実行しても乱数系列は同じになる。
'''
script['sh_code']='''
mnewrand a=rand S=1 o=rsl1.csv
'''
script['py_code']='''
nm.mnewrand(a="rand", S="1", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='整数乱数'
script['comment']='''
最小値が0、最大値が1000、乱数の種が1の整数乱数を5行作成する。
'''
script['sh_code']='''
mnewrand a=rand -int max=1000 min=0 l=5 S=1 o=rsl2.csv
'''
script['py_code']='''
nm.mnewrand(a="rand", int=True, max="1000", min="0", l="5", S="1", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='ヘッダ行なしで出力'
script['comment']='''
``nfn=True`` でヘッダーなしのデータが生成される。
'''
script['sh_code']='''
mnewrand -nfn l=5 S=1 o=rsl3.csv
'''
script['py_code']='''
nm.mnewrand(nfn=True, l="5", S="1", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

