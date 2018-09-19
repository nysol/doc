# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mnewstr'

############################### IDATA
db['idatas']=[]

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``custNo`` と ``A0001`` という文字列データを5行作成し、 ``attribute,code`` という名前の項目名で出力する。
'''
script['sh_code']='''
mnewstr a=attribute,code v=custNo,A0001 l=5 o=rsl1.csv
'''
script['py_code']='''
nm.mnewstr(a="attribute,code", v="custNo,A0001", l="5", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

